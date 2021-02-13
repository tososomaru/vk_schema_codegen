from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class CheckTokenResponse(BaseResponse):
	response: Optional["CheckTokenResponseModel"] = None


class GetAppBalanceResponse(BaseResponse):
	response: Optional["GetAppBalanceResponseModel"] = None


class GetSMSHistoryResponse(BaseResponse):
	response: Optional["GetSMSHistoryResponseModel"] = None


class GetTransactionsHistoryResponse(BaseResponse):
	response: Optional["GetTransactionsHistoryResponseModel"] = None


class GetUserLevelResponse(BaseResponse):
	response: Optional["GetUserLevelResponseModel"] = None


class GiveEventStickerResponse(BaseResponse):
	response: Optional["GiveEventStickerResponseModel"] = None


class SendNotificationResponse(BaseResponse):
	response: Optional["SendNotificationResponseModel"] = None


CheckTokenResponseModelModel = None


GetAppBalanceResponseModelModel = None


GetSMSHistoryResponseModelModel = array


GetTransactionsHistoryResponseModelModel = array


GetUserLevelResponseModelModel = array


GiveEventStickerResponseModelModel = array


SendNotificationResponseModelModel = array

CheckTokenResponse.update_forward_refs()
GetAppBalanceResponse.update_forward_refs()
GetSMSHistoryResponse.update_forward_refs()
GetTransactionsHistoryResponse.update_forward_refs()
GetUserLevelResponse.update_forward_refs()
GiveEventStickerResponse.update_forward_refs()
SendNotificationResponse.update_forward_refs()
