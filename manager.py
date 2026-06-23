import json
import logging
import os
import sys

from game.attack import AttackCache
from game.reports import ReportCache


class VillageManager:
    @staticmethod
    def farm_manager(verbose=False, clean_reports=False):
        logger = logging.getLogger("Menedżer farmy")
        with open("config.json", "r") as f:
            config = json.load(f)

        if verbose:
            logger.info("Wsie: %d", len(config["villages"]))
        attacks = AttackCache.cache_grab()
        reports = ReportCache.cache_grab()

        if verbose:
            logger.info("Raporty: %d", len(reports))
            logger.info("Farmy: %d", len(attacks))
        t = {"drewno": 0, "\u017celazo": 0, "kamią": 0}
        for farm in attacks:
            data = attacks[farm]

            num_attack = []
            loot = {"wood": 0, "iron": 0, "stone": 0}
            total_loss_count = 0
            total_sent_count = 0
            for rep in reports:
                if reports[rep]["dest"] == farm and reports[rep]["type"] == "attack":
                    for unit in reports[rep]["extra"]["units_sent"]:
                        total_sent_count += reports[rep]["extra"]["units_sent"][unit]
                    for unit in reports[rep]["extra"]["units_losses"]:
                        total_loss_count += reports[rep]["extra"]["units_losses"][unit]
                    try:
                        res = reports[rep]["extra"]["loot"]
                        for r in res:
                            loot[r] = loot[r] + int(res[r])
                            t[r] = t[r] + int(res[r])
                        num_attack.append(reports[rep])
                    except:
                        pass
            percentage_lost = 0

            if total_sent_count > 0:
                percentage_lost = total_loss_count / total_sent_count * 100

            perf = ""
            if data["high_profile"]:
                perf = "Wysoki profil "
            if "low_profile" in data and data["low_profile"]:
                perf = "Niski profil "
            if verbose:
                logger.info(
                    "%sWieś farmy %s zaatakowana %d razy - Całkowity łup: %s - Całkowita strata jednostek: %d (%.2f)",
                    perf, farm, len(num_attack), str(loot), total_loss_count, percentage_lost
                )
            if len(num_attack):
                total = 0
                for k in loot:
                    total += loot[k]
                if len(num_attack) > 3:
                    if total / len(num_attack) < 100 and (
                            "low_profile" not in data or not data["low_profile"]
                    ):
                        if verbose:
                            logger.info(
                                "Farma %s ma bardzo mało zasobów (%d średnio razem), przedłużanie czasu farmy",
                                farm, total / len(num_attack)
                            )
                        data["low_profile"] = True
                        AttackCache.set_cache(farm, data)
                    elif total / len(num_attack) > 500 and (
                            "high_profile" not in data or not data["high_profile"]
                    ):
                        if verbose:
                            logger.info(
                                "Farma %s ma bardzo dużo zasobów (%d średnio razem), ustawianie na wysoki profil",
                                farm, total / len(num_attack)
                            )
                        data["high_profile"] = True
                        AttackCache.set_cache(farm, data)

            if percentage_lost > 20 and not data["low_profile"]:
                logger.warning(f"Niebezpieczne {percentage_lost} procent straconych jednostek! Przedłużanie czasu farmy")
                data["low_profile"] = True
                data["high_profile"] = False
                AttackCache.set_cache(farm, data)
            if percentage_lost > 50 and len(num_attack) > 10:
                logger.critical("Farma wydaje się zbyt niebezpieczna/nieopłacalna do farmy. Ustawianie bezpiecznego na false!")
                data["safe"] = False
                AttackCache.set_cache(farm, data)

        if verbose:
            logger.info("Total loot: %s" % t)

        if clean_reports:
            list_of_files = sorted(["./cache/reports/" + f for f in os.listdir("./cache/reports/")],
                                   key=os.path.getctime)

            logger.info(f"Znaleziono {len(list_of_files)} plików")

            while len(list_of_files) > clean_reports:
                oldest_file = list_of_files.pop(0)
                logger.info(f"Usuwanie starego raportu ({oldest_file})")
                os.remove(os.path.abspath(oldest_file))


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout)
    VillageManager.farm_manager(verbose=True)
