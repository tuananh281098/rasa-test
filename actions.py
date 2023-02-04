from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return 'action_default_fallback'

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_default")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]
class ActionShowHelp(Action):
    
    def name(self) -> Text:
        return "action_show_help"
    
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        list_ques = {
            "Rút tiền như thế nào",
            "Làm thế nào khi bị nuốt thẻ",
            "Chuyển khoản thế nào",
            "Làm thế nào để nạp tiền",
            "Phí rút tiền",
            "Làm thế nào khi rút tiền lỗi",
            "Cách kiểm tra số dư tài khoản",
            "Cách đổi mã pin",
            "Hạn mức rút tiền",
            "Lãi suất tiết kiệm",
        }
        res = "Đây là một số câu hỏi tôi có thể trả lời:\n- " + "\n- ".join(list_ques)
        dispatcher.utter_message(text=res)
        return []