from common.data.post_breach_consts import POST_BREACH_SIGNED_SCRIPT_PROXY_EXEC
from monkey_island.cc.services.attack.technique_reports.pba_technique import \
    PostBreachTechnique

__author__ = "shreyamalviya"


class T1216(PostBreachTechnique):
    tech_id = "T1216"
    unscanned_msg = "Monkey didn't attempt to execute an arbitrary file with the help of a " +\
                    "pre-existing signed script since it didn't run on any Windows machines."
    scanned_msg = "Monkey attempted to execute an arbitrary file with the help of a " +\
                  "pre-existing signed script on Windows but failed."
    used_msg = "Monkey executed an arbitrary file with the help of a pre-existing signed script on Windows."
    pba_names = [POST_BREACH_SIGNED_SCRIPT_PROXY_EXEC]
