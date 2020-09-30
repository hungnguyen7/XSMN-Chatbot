# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted
import requests
import json
import feedparser

# Ham lay ket qua xo so va tra ve. Ten ham la action_get_lottery
class action_get_lottery(Action):
    def name(self):
        # Tra ve ten ham
        return 'action_get_lottery'
    def run(self, dispatcher, tracker, domain):
        url = 'https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss'
        # Tien hanh lay thong tin tu URL
        feed_content = feedparser.parse(url)
        # Lay ket qua so xo moi nhat
        first_node = feed_content['entries']
        # Lay thong tin ve ngay va chi tiet cac giai
        return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
        # Tra ve va hien thi cho nguoi dung
        dispatcher.utter_message(return_msg)
        return []
