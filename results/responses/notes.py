from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddResponse(BaseResponse):
	response: Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


AddResponseModel = int


CreateCommentResponseModel = int


GetByIdResponseModel = Optional[Notesnote]


class GetCommentsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None

AddResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetResponse.update_forward_refs()
