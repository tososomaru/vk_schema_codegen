from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetPagesResponse(BaseResponse):
	response: Optional["GetPagesResponseModel"] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	posts: Optional["array"] = None


class GetPagesResponseModel(BaseResponse):
	count: Optional["integer"] = None
	pages: Optional["array"] = None

GetCommentsResponse.update_forward_refs()
GetPagesResponse.update_forward_refs()
