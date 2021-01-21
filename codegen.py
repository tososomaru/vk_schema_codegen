

class AccountAccountCounters(BaseModel):
	"""VK Object AccountAccountCounters

	app_requests - New app requests number
	events - New events number
	faves - New faves number
	friends - New friends requests number
	friends_suggestions - New friends suggestions number
	friends_recommendations - New friends recommendations number
	gifts - New gifts number
	groups - New groups number
	menu_discover_badge - 
	menu_clips_badge - 
	messages - New messages number
	memories - New memories number
	notes - New notes number
	notifications - New notifications number
	photos - New photo tags number
	sdk - New sdk number
	"""
	app_requests = None
	events = None
	faves = None
	friends = None
	friends_suggestions = None
	friends_recommendations = None
	gifts = None
	groups = None
	menu_discover_badge = None
	menu_clips_badge = None
	messages = None
	memories = None
	notes = None
	notifications = None
	photos = None
	sdk = None


class AccountInfo(BaseModel):
	"""VK Object AccountInfo

	wishlists_ae_promo_banner_show - 
	2fa_required - Two factor authentication is enabled
	country - Country code
	https_required - Information whether HTTPS-only is enabled
	intro - Information whether user has been processed intro
	show_vk_apps_intro - 
	mini_apps_ads_slot_id - Ads slot id for MyTarget
	qr_promotion - 
	link_redirects - 
	lang - Language ID
	no_wall_replies - Information whether wall comments should be hidden
	own_posts_default - Information whether only owners posts should be shown
	subscriptions - 
	"""
	wishlists_ae_promo_banner_show = None
	_2fa_required = None
	country = None
	https_required = None
	intro = None
	show_vk_apps_intro = None
	mini_apps_ads_slot_id = None
	qr_promotion = None
	link_redirects = None
	lang = None
	no_wall_replies = None
	own_posts_default = None
	subscriptions = None


class AccountNAmeRequest(BaseModel):
	"""VK Object AccountNAmeRequest

	first_name - First name in request
	id - Request ID needed to cancel the request
	last_name - Last name in request
	status - 
	lang - Text to display to user
	link_href - href for link in lang field
	link_label - label to display for link in lang field
	"""
	first_name = None
	id = None
	last_name = None
	status = None
	lang = None
	link_href = None
	link_label = None


class AccountNAmeRequestStAtus(enum.Enum):
	"""VK Object AccountNAmeRequestStAtus

	"""
	SUCCESS = "success"
	PROCESSING = "processing"
	DECLINED = "declined"
	WAS_ACCEPTED = "was_accepted"
	WAS_DECLINED = "was_declined"
	DECLINED_WITH_LINK = "declined_with_link"
	RESPONSE = "response"
	RESPONSE_WITH_LINK = "response_with_link"


class AccountOffer(BaseModel):
	"""VK Object AccountOffer

	description - Offer description
	id - Offer ID
	img - URL of the preview image
	instruction - Instruction how to process the offer
	instruction_html - Instruction how to process the offer (HTML format)
	price - Offer price
	short_description - Offer short description
	tag - Offer tag
	title - Offer title
	currency_amount - Currency amount
	link_id - Link id
	link_type - Link type
	"""
	description = None
	id = None
	img = None
	instruction = None
	instruction_html = None
	price = None
	short_description = None
	tag = None
	title = None
	currency_amount = None
	link_id = None
	link_type = None


class AccountPushConversAtions(BaseModel):
	"""VK Object AccountPushConversAtions

	count - Items count
	items - 
	"""
	count = None
	items = None


class AccountPushConversAtionsItem(BaseModel):
	"""VK Object AccountPushConversAtionsItem

	disabled_until - Time until that notifications are disabled in seconds
	peer_id - Peer ID
	sound - Information whether the sound are enabled
	"""
	disabled_until = None
	peer_id = None
	sound = None


class AccountPushPArAms(BaseModel):
	"""VK Object AccountPushPArAms

	"""
	msg = None
	chat = None
	like = None
	repost = None
	comment = None
	mention = None
	reply = None
	new_post = None
	wall_post = None
	wall_publish = None
	friend = None
	friend_found = None
	friend_accepted = None
	group_invite = None
	group_accepted = None
	birthday = None
	event_soon = None
	app_request = None
	sdk_open = None


class AccountPushPArAmsMode(enum.Enum):
	"""VK Object AccountPushPArAmsMode

	"""
	ON = "on"
	OFF = "off"
	NO_SOUND = "no_sound"
	NO_TEXT = "no_text"


class AccountPushPArAmsOnoff(enum.Enum):
	"""VK Object AccountPushPArAmsOnoff

	"""
	ON = "on"
	OFF = "off"


class AccountPushPArAmsSettings(enum.Enum):
	"""VK Object AccountPushPArAmsSettings

	"""
	ON = "on"
	OFF = "off"
	FR_OF_FR = "fr_of_fr"


class AccountPushSettings(BaseModel):
	"""VK Object AccountPushSettings

	disabled - Information whether notifications are disabled
	disabled_until - Time until that notifications are disabled in Unixtime
	settings - 
	conversations - 
	"""
	disabled = None
	disabled_until = None
	settings = None
	conversations = None


class AccountUserSettings(BaseModel):
	"""VK Object AccountUserSettings

	photo_200 - URL of square photo of the user with 200 pixels in width
	is_service_account - flag about service account
	"""
	photo_200 = None
	is_service_account = None


class AccountUserSettingsInterest(BaseModel):
	"""VK Object AccountUserSettingsInterest

	"""
	title = None
	value = None


class AccountUserSettingsInterests(BaseModel):
	"""VK Object AccountUserSettingsInterests

	"""
	activities = None
	interests = None
	music = None
	tv = None
	movies = None
	books = None
	games = None
	quotes = None
	about = None


class AddressesFields(enum.Enum):
	"""VK Object AddressesFields

	"""
	ID = "id"
	TITLE = "title"
	ADDRESS = "address"
	ADDITIONAL_ADDRESS = "additional_address"
	COUNTRY_ID = "country_id"
	CITY_ID = "city_id"
	METRO_STATION_ID = "metro_station_id"
	LATITUDE = "latitude"
	LONGITUDE = "longitude"
	DISTANCE = "distance"
	WORK_INFO_STATUS = "work_info_status"
	TIMETABLE = "timetable"
	PHONE = "phone"
	TIME_OFFSET = "time_offset"


class AdsAccessRole(enum.Enum):
	"""VK Object AdsAccessRole

	"""
	ADMIN = "admin"
	MANAGER = "manager"
	REPORTS = "reports"


class AdsAccessRolePublic(enum.Enum):
	"""VK Object AdsAccessRolePublic

	"""
	MANAGER = "manager"
	REPORTS = "reports"


class AdsAccesses(BaseModel):
	"""VK Object AdsAccesses

	client_id - Client ID
	role - 
	"""
	client_id = None
	role = None


class AdsAccount(BaseModel):
	"""VK Object AdsAccount

	access_role - 
	account_id - Account ID
	account_status - Information whether account is active
	account_type - 
	account_name - Account name
	can_view_budget - Can user view account budget
	"""
	access_role = None
	account_id = None
	account_status = None
	account_type = None
	account_name = None
	can_view_budget = None


class AdsAccountType(enum.Enum):
	"""VK Object AdsAccountType

	"""
	GENERAL = "general"
	AGENCY = "agency"


class AdsAd(BaseModel):
	"""VK Object AdsAd

	ad_format - Ad format
	ad_platform - Ad platform
	all_limit - Total limit
	approved - 
	campaign_id - Campaign ID
	category1_id - Category ID
	category2_id - Additional category ID
	cost_type - 
	cpc - Cost of a click, kopecks
	cpm - Cost of 1000 impressions, kopecks
	cpa - Cost of an action, kopecks
	ocpm - Cost of 1000 impressions optimized, kopecks
	autobidding_max_cost - Max cost of target actions for autobidding, kopecks
	disclaimer_medical - Information whether disclaimer is enabled
	disclaimer_specialist - Information whether disclaimer is enabled
	disclaimer_supplements - Information whether disclaimer is enabled
	id - Ad ID
	impressions_limit - Impressions limit
	impressions_limited - Information whether impressions are limited
	name - Ad title
	status - 
	video - Information whether the ad is a video
	"""
	ad_format = None
	ad_platform = None
	all_limit = None
	approved = None
	campaign_id = None
	category1_id = None
	category2_id = None
	cost_type = None
	cpc = None
	cpm = None
	cpa = None
	ocpm = None
	autobidding_max_cost = None
	disclaimer_medical = None
	disclaimer_specialist = None
	disclaimer_supplements = None
	id = None
	impressions_limit = None
	impressions_limited = None
	name = None
	status = None
	video = None


class AdsAdApproved(enum.IntEnum):
	"""VK Object AdsAdApproved

	"""
	not moderated = 0
	pending moderation = 1
	approved = 2
	rejected = 3


class AdsAdCostType(enum.IntEnum):
	"""VK Object AdsAdCostType

	"""
	per clicks = 0
	per impressions = 1
	per actions = 2
	per impressions optimized = 3


class AdsAdLAyout(BaseModel):
	"""VK Object AdsAdLAyout

	ad_format - Ad format
	campaign_id - Campaign ID
	cost_type - 
	description - Ad description
	id - Ad ID
	image_src - Image URL
	image_src_2x - URL of the preview image in double size
	link_domain - Domain of advertised object
	link_url - URL of advertised object
	preview_link - link to preview an ad as it is shown on the website
	title - Ad title
	video - Information whether the ad is a video
	"""
	ad_format = None
	campaign_id = None
	cost_type = None
	description = None
	id = None
	image_src = None
	image_src_2x = None
	link_domain = None
	link_url = None
	preview_link = None
	title = None
	video = None


class AdsAdStAtus(enum.IntEnum):
	"""VK Object AdsAdStAtus

	"""
	stopped = 0
	started = 1
	deleted = 2


class AdsCAmpAign(BaseModel):
	"""VK Object AdsCAmpAign

	all_limit - Campaign's total limit, rubles
	day_limit - Campaign's day limit, rubles
	id - Campaign ID
	name - Campaign title
	start_time - Campaign start time, as Unixtime
	status - 
	stop_time - Campaign stop time, as Unixtime
	type - 
	"""
	all_limit = None
	day_limit = None
	id = None
	name = None
	start_time = None
	status = None
	stop_time = None
	type = None


class AdsCAmpAignStAtus(enum.IntEnum):
	"""VK Object AdsCAmpAignStAtus

	"""
	stopped = 0
	started = 1
	deleted = 2


class AdsCAmpAignType(enum.Enum):
	"""VK Object AdsCAmpAignType

	"""
	NORMAL = "normal"
	VK_APPS_MANAGED = "vk_apps_managed"
	MOBILE_APPS = "mobile_apps"
	PROMOTED_POSTS = "promoted_posts"


class AdsCAtegory(BaseModel):
	"""VK Object AdsCAtegory

	id - Category ID
	name - Category name
	subcategories - 
	"""
	id = None
	name = None
	subcategories = None


class AdsClient(BaseModel):
	"""VK Object AdsClient

	all_limit - Client's total limit, rubles
	day_limit - Client's day limit, rubles
	id - Client ID
	name - Client name
	"""
	all_limit = None
	day_limit = None
	id = None
	name = None


class AdsCriteriA(BaseModel):
	"""VK Object AdsCriteriA

	age_from - Age from
	age_to - Age to
	apps - Apps IDs
	apps_not - Apps IDs to except
	birthday - Days to birthday
	cities - Cities IDs
	cities_not - Cities IDs to except
	country - Country ID
	districts - Districts IDs
	groups - Communities IDs
	interest_categories - Interests categories IDs
	interests - Interests
	paying - Information whether the user has proceeded VK payments before
	positions - Positions IDs
	religions - Religions IDs
	retargeting_groups - Retargeting groups IDs
	retargeting_groups_not - Retargeting groups IDs to except
	school_from - School graduation year from
	school_to - School graduation year to
	schools - Schools IDs
	sex - 
	stations - Stations IDs
	statuses - Relationship statuses
	streets - Streets IDs
	travellers - Travellers only
	uni_from - University graduation year from
	uni_to - University graduation year to
	user_browsers - Browsers
	user_devices - Devices
	user_os - Operating systems
	"""
	age_from = None
	age_to = None
	apps = None
	apps_not = None
	birthday = None
	cities = None
	cities_not = None
	country = None
	districts = None
	groups = None
	interest_categories = None
	interests = None
	paying = None
	positions = None
	religions = None
	retargeting_groups = None
	retargeting_groups_not = None
	school_from = None
	school_to = None
	schools = None
	sex = None
	stations = None
	statuses = None
	streets = None
	travellers = None
	uni_from = None
	uni_to = None
	user_browsers = None
	user_devices = None
	user_os = None


class AdsCriteriASex(enum.IntEnum):
	"""VK Object AdsCriteriASex

	"""
	any = 0
	male = 1
	female = 2


class AdsDemoStAts(BaseModel):
	"""VK Object AdsDemoStAts

	id - Object ID
	stats - 
	type - 
	"""
	id = None
	stats = None
	type = None


class AdsDemostAtsFormAt(BaseModel):
	"""VK Object AdsDemostAtsFormAt

	age - 
	cities - 
	day - Day as YYYY-MM-DD
	month - Month as YYYY-MM
	overall - 1 if period=overall
	sex - 
	sex_age - 
	"""
	age = None
	cities = None
	day = None
	month = None
	overall = None
	sex = None
	sex_age = None


class AdsFloodStAts(BaseModel):
	"""VK Object AdsFloodStAts

	left - Requests left
	refresh - Time to refresh in seconds
	"""
	left = None
	refresh = None


class AdsLinkStAtus(BaseModel):
	"""VK Object AdsLinkStAtus

	description - Reject reason
	redirect_url - URL
	status - Link status
	"""
	description = None
	redirect_url = None
	status = None


class AdsLookAlikeRequest(BaseModel):
	"""VK Object AdsLookAlikeRequest

	id - Lookalike request ID
	create_time - Lookalike request create time, as Unixtime
	update_time - Lookalike request update time, as Unixtime
	scheduled_delete_time - Time by which lookalike request would be deleted, as Unixtime
	status - Lookalike request status
	source_type - Lookalike request source type
	source_retargeting_group_id - Retargeting group id, which was used as lookalike seed
	source_name - Lookalike request seed name (retargeting group name)
	audience_count - Lookalike request seed audience size
	save_audience_levels - 
	"""
	id = None
	create_time = None
	update_time = None
	scheduled_delete_time = None
	status = None
	source_type = None
	source_retargeting_group_id = None
	source_name = None
	audience_count = None
	save_audience_levels = None


class AdsLookAlikeRequestSAveAudienceLevel(BaseModel):
	"""VK Object AdsLookAlikeRequestSAveAudienceLevel

	level - Save audience level id, which is used in save audience queries
	audience_count - Saved audience audience size for according level
	"""
	level = None
	audience_count = None


class AdsMusiciAn(BaseModel):
	"""VK Object AdsMusiciAn

	id - Targeting music artist ID
	name - Music artist name
	avatar - Music artist photo
	"""
	id = None
	name = None
	avatar = None


class AdsObjectType(enum.Enum):
	"""VK Object AdsObjectType

	"""
	AD = "ad"
	CAMPAIGN = "campaign"
	CLIENT = "client"
	OFFICE = "office"


class AdsPArAgrAphs(BaseModel):
	"""VK Object AdsPArAgrAphs

	paragraph - Rules paragraph
	"""
	paragraph = None


class AdsPromotedPostReAch(BaseModel):
	"""VK Object AdsPromotedPostReAch

	hide - Hides amount
	id - Object ID from 'ids' parameter
	join_group - Community joins
	links - Link clicks
	reach_subscribers - Subscribers reach
	reach_total - Total reach
	report - Reports amount
	to_group - Community clicks
	unsubscribe - 'Unsubscribe' events amount
	video_views_100p - Video views for 100 percent
	video_views_25p - Video views for 25 percent
	video_views_3s - Video views for 3 seconds
	video_views_50p - Video views for 50 percent
	video_views_75p - Video views for 75 percent
	video_views_start - Video starts
	"""
	hide = None
	id = None
	join_group = None
	links = None
	reach_subscribers = None
	reach_total = None
	report = None
	to_group = None
	unsubscribe = None
	video_views_100p = None
	video_views_25p = None
	video_views_3s = None
	video_views_50p = None
	video_views_75p = None
	video_views_start = None


class AdsRejectReAson(BaseModel):
	"""VK Object AdsRejectReAson

	comment - Comment text
	rules - 
	"""
	comment = None
	rules = None


class AdsRules(BaseModel):
	"""VK Object AdsRules

	paragraphs - 
	title - Comment
	"""
	paragraphs = None
	title = None


class AdsStAts(BaseModel):
	"""VK Object AdsStAts

	id - Object ID
	stats - 
	type - 
	views_times - 
	"""
	id = None
	stats = None
	type = None
	views_times = None


class AdsStAtsAge(BaseModel):
	"""VK Object AdsStAtsAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Age interval
	"""
	clicks_rate = None
	impressions_rate = None
	value = None


class AdsStAtsCities(BaseModel):
	"""VK Object AdsStAtsCities

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	name - City name
	value - City ID
	"""
	clicks_rate = None
	impressions_rate = None
	name = None
	value = None


class AdsStAtsFormAt(BaseModel):
	"""VK Object AdsStAtsFormAt

	clicks - Clicks number
	day - Day as YYYY-MM-DD
	impressions - Impressions number
	join_rate - Events number
	month - Month as YYYY-MM
	overall - 1 if period=overall
	reach - Reach 
	spent - Spent funds
	video_clicks_site - Clickthoughs to the advertised site
	video_views - Video views number
	video_views_full - Video views (full video)
	video_views_half - Video views (half of video)
	"""
	clicks = None
	day = None
	impressions = None
	join_rate = None
	month = None
	overall = None
	reach = None
	spent = None
	video_clicks_site = None
	video_views = None
	video_views_full = None
	video_views_half = None


class AdsStAtsSex(BaseModel):
	"""VK Object AdsStAtsSex

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - 
	"""
	clicks_rate = None
	impressions_rate = None
	value = None


class AdsStAtsSexAge(BaseModel):
	"""VK Object AdsStAtsSexAge

	clicks_rate - Clicks rate
	impressions_rate - Impressions rate
	value - Sex and age interval
	"""
	clicks_rate = None
	impressions_rate = None
	value = None


class AdsStAtsSexVAlue(enum.Enum):
	"""VK Object AdsStAtsSexVAlue

	"""
	F = "f"
	M = "m"


class AdsStAtsViewsTimes(BaseModel):
	"""VK Object AdsStAtsViewsTimes

	"""
	views_ads_times_1 = None
	views_ads_times_2 = None
	views_ads_times_3 = None
	views_ads_times_4 = None
	views_ads_times_5 = None
	views_ads_times_6 = None
	views_ads_times_7 = None
	views_ads_times_8 = None
	views_ads_times_9 = None
	views_ads_times_10 = None
	views_ads_times_11_plus = None


class AdsTArgSettings(BaseModel):
	"""VK Object AdsTArgSettings

	id - Ad ID
	campaign_id - Campaign ID
	"""
	id = None
	campaign_id = None


class AdsTArgStAts(BaseModel):
	"""VK Object AdsTArgStAts

	audience_count - Audience
	recommended_cpc - Recommended CPC value for 50% reach (old format)
	recommended_cpm - Recommended CPM value for 50% reach (old format)
	recommended_cpc_50 - Recommended CPC value for 50% reach
	recommended_cpm_50 - Recommended CPM value for 50% reach
	recommended_cpc_70 - Recommended CPC value for 70% reach
	recommended_cpm_70 - Recommended CPM value for 70% reach
	recommended_cpc_90 - Recommended CPC value for 90% reach
	recommended_cpm_90 - Recommended CPM value for 90% reach
	"""
	audience_count = None
	recommended_cpc = None
	recommended_cpm = None
	recommended_cpc_50 = None
	recommended_cpm_50 = None
	recommended_cpc_70 = None
	recommended_cpm_70 = None
	recommended_cpc_90 = None
	recommended_cpm_90 = None


class AdsTArgSuggestions(BaseModel):
	"""VK Object AdsTArgSuggestions

	id - Object ID
	name - Object name
	"""
	id = None
	name = None


class AdsTArgSuggestionsCities(BaseModel):
	"""VK Object AdsTArgSuggestionsCities

	id - Object ID
	name - Object name
	parent - Parent object
	"""
	id = None
	name = None
	parent = None


class AdsTArgSuggestionsRegions(BaseModel):
	"""VK Object AdsTArgSuggestionsRegions

	id - Object ID
	name - Object name
	type - Object type
	"""
	id = None
	name = None
	type = None


class AdsTArgSuggestionsSchools(BaseModel):
	"""VK Object AdsTArgSuggestionsSchools

	desc - Full school title
	id - School ID
	name - School title
	parent - City name
	type - 
	"""
	desc = None
	id = None
	name = None
	parent = None
	type = None


class AdsTArgSuggestionsSchoolsType(enum.Enum):
	"""VK Object AdsTArgSuggestionsSchoolsType

	"""
	SCHOOL = "school"
	UNIVERSITY = "university"
	FACULTY = "faculty"
	CHAIR = "chair"


class AdsTArgetGroup(BaseModel):
	"""VK Object AdsTArgetGroup

	audience_count - Audience
	domain - Site domain
	id - Group ID
	lifetime - Number of days for user to be in group
	name - Group name
	pixel - Pixel code
	"""
	audience_count = None
	domain = None
	id = None
	lifetime = None
	name = None
	pixel = None


class AdsUpdAteOfficeUsersResult(BaseModel):
	"""VK Object AdsUpdAteOfficeUsersResult

	"""
	user_id = None
	is_success = None
	error = None


class AdsUserSpecificAtion(BaseModel):
	"""VK Object AdsUserSpecificAtion

	"""
	user_id = None
	role = None
	grant_access_to_all_clients = None
	client_ids = None
	view_budget = None


class AdsUserSpecificAtionCutted(BaseModel):
	"""VK Object AdsUserSpecificAtionCutted

	"""
	user_id = None
	role = None
	client_id = None
	view_budget = None


class AdsUsers(BaseModel):
	"""VK Object AdsUsers

	accesses - 
	user_id - User ID
	"""
	accesses = None
	user_id = None


class AdswebGetAdCAtegoriesResponseCAtegoriesCAtegory(BaseModel):
	"""VK Object AdswebGetAdCAtegoriesResponseCAtegoriesCAtegory

	"""
	id = None
	name = None


class AdswebGetAdUnitsResponseAdUnitsAdUnit(BaseModel):
	"""VK Object AdswebGetAdUnitsResponseAdUnitsAdUnit

	"""
	id = None
	site_id = None
	name = None


class AdswebGetFrAudHistoryResponseEntriesEntry(BaseModel):
	"""VK Object AdswebGetFrAudHistoryResponseEntriesEntry

	"""
	site_id = None
	day = None


class AdswebGetSitesResponseSitesSite(BaseModel):
	"""VK Object AdswebGetSitesResponseSitesSite

	"""
	id = None
	status_user = None
	status_moder = None
	domains = None


class AdswebGetStAtisticsResponseItemsItem(BaseModel):
	"""VK Object AdswebGetStAtisticsResponseItemsItem

	"""
	site_id = None
	ad_unit_id = None
	overall_count = None
	months_count = None
	month_min = None
	month_max = None
	days_count = None
	day_min = None
	day_max = None
	hours_count = None
	hour_min = None
	hour_max = None


class AppWidgetsPhoto(BaseModel):
	"""VK Object AppWidgetsPhoto

	id - Image ID
	images - 
	"""
	id = None
	images = None


class AppWidgetsPhotos(BaseModel):
	"""VK Object AppWidgetsPhotos

	"""
	count = None
	items = None


class AppsApp(BaseModel):
	"""VK Object AppsApp

	author_url - Application author's URL
	banner_1120 - URL of the app banner with 1120 px in width
	banner_560 - URL of the app banner with 560 px in width
	icon_16 - URL of the app icon with 16 px in width
	is_new - Is new flag
	push_enabled - Is push enabled
	screen_orientation - Screen orientation
	friends - 
	catalog_position - Catalog position
	description - Application description
	genre - Genre name
	genre_id - Genre ID
	international - Information whether the application is multilanguage
	is_in_catalog - Information whether application is in mobile catalog
	leaderboard_type - 
	members_count - Members number
	platform_id - Application ID in store
	published_date - Date when the application has been published in Unixtime
	screen_name - Screen name
	section - Application section name
	"""
	author_url = None
	banner_1120 = None
	banner_560 = None
	icon_16 = None
	is_new = None
	push_enabled = None
	screen_orientation = None
	friends = None
	catalog_position = None
	description = None
	genre = None
	genre_id = None
	international = None
	is_in_catalog = None
	leaderboard_type = None
	members_count = None
	platform_id = None
	published_date = None
	screen_name = None
	section = None


class AppsAppLeAderboArdType(enum.IntEnum):
	"""VK Object AppsAppLeAderboArdType

	"""
	not supported = 0
	levels = 1
	points = 2


class AppsAppMin(BaseModel):
	"""VK Object AppsAppMin

	type - 
	id - Application ID
	title - Application title
	author_owner_id - Application author's ID
	is_installed - Is application installed
	icon_139 - URL of the app icon with 139 px in width
	icon_150 - URL of the app icon with 150 px in width
	icon_278 - URL of the app icon with 278 px in width
	icon_576 - URL of the app icon with 576 px in width
	background_loader_color - Hex color code without hash sign
	loader_icon - SVG data
	icon_75 - URL of the app icon with 75 px in width
	"""
	type = None
	id = None
	title = None
	author_owner_id = None
	is_installed = None
	icon_139 = None
	icon_150 = None
	icon_278 = None
	icon_576 = None
	background_loader_color = None
	loader_icon = None
	icon_75 = None


class AppsAppType(enum.Enum):
	"""VK Object AppsAppType

	"""
	APP = "app"
	GAME = "game"
	SITE = "site"
	STANDALONE = "standalone"
	VK_APP = "vk_app"
	COMMUNITY_APP = "community_app"
	HTML5_GAME = "html5_game"
	MINI_APP = "mini_app"


class AppsLeAderboArd(BaseModel):
	"""VK Object AppsLeAderboArd

	level - Level
	points - Points number
	score - Score number
	user_id - User ID
	"""
	level = None
	points = None
	score = None
	user_id = None


class AppsScope(BaseModel):
	"""VK Object AppsScope

	name - Scope name
	title - Scope title
	"""
	name = None
	title = None


class AudioAudio(BaseModel):
	"""VK Object AudioAudio

	access_key - Access key for the audio
	artist - Artist name
	id - Audio ID
	owner_id - Audio owner's ID
	title - Title
	url - URL of mp3 file
	duration - Duration in seconds
	date - Date when uploaded
	album_id - Album ID
	genre_id - Genre ID
	performer - Performer name
	"""
	access_key = None
	artist = None
	id = None
	owner_id = None
	title = None
	url = None
	duration = None
	date = None
	album_id = None
	genre_id = None
	performer = None


class BaseBoolInt(enum.IntEnum):
	"""VK Object BaseBoolInt

	"""
	no = 0
	yes = 1


class BaseCity(BaseModel):
	"""VK Object BaseCity

	id - City ID
	title - City title
	"""
	id = None
	title = None


class BaseCommentsInfo(BaseModel):
	"""VK Object BaseCommentsInfo

	can_post - Information whether current user can comment the post
	count - Comments number
	groups_can_post - Information whether groups can comment the post
	donut - 
	"""
	can_post = None
	count = None
	groups_can_post = None
	donut = None


class BaseCountry(BaseModel):
	"""VK Object BaseCountry

	id - Country ID
	title - Country title
	"""
	id = None
	title = None


class BaseCropPhoto(BaseModel):
	"""VK Object BaseCropPhoto

	"""
	photo = None
	crop = None
	rect = None


class BaseCropPhotoCrop(BaseModel):
	"""VK Object BaseCropPhotoCrop

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x = None
	y = None
	x2 = None
	y2 = None


class BaseCropPhotoRect(BaseModel):
	"""VK Object BaseCropPhotoRect

	x - Coordinate X of the left upper corner
	y - Coordinate Y of the left upper corner
	x2 - Coordinate X of the right lower corner
	y2 - Coordinate Y of the right lower corner
	"""
	x = None
	y = None
	x2 = None
	y2 = None


class BaseError(BaseModel):
	"""VK Object BaseError

	error_code - Error code
	error_subcode - Error subcode
	error_msg - Error message
	error_text - Localized error message
	request_params - 
	"""
	error_code = None
	error_subcode = None
	error_msg = None
	error_text = None
	request_params = None


class BaseGeo(BaseModel):
	"""VK Object BaseGeo

	coordinates - 
	place - 
	showmap - Information whether a map is showed
	type - Place type
	"""
	coordinates = None
	place = None
	showmap = None
	type = None


class BaseGeoCoordinates(BaseModel):
	"""VK Object BaseGeoCoordinates

	"""
	latitude = None
	longitude = None


class BaseGradientPoint(BaseModel):
	"""VK Object BaseGradientPoint

	color - Hex color code without #
	position - Point position
	"""
	color = None
	position = None


class BaseImage(BaseModel):
	"""VK Object BaseImage

	id - 
	height - Image height
	url - Image url
	width - Image width
	"""
	id = None
	height = None
	url = None
	width = None


class BaseLikes(BaseModel):
	"""VK Object BaseLikes

	count - Likes number
	user_likes - Information whether current user likes the photo
	"""
	count = None
	user_likes = None


class BaseLikesInfo(BaseModel):
	"""VK Object BaseLikesInfo

	can_like - Information whether current user can like the post
	can_publish - Information whether current user can repost
	count - Likes number
	user_likes - Information whether current uer has liked the post
	"""
	can_like = None
	can_publish = None
	count = None
	user_likes = None


class BaseLink(BaseModel):
	"""VK Object BaseLink

	application - 
	button - 
	caption - Link caption
	description - Link description
	id - Link ID
	is_favorite - 
	photo - 
	preview_page - String ID of the page with article preview
	preview_url - URL of the page with article preview
	product - 
	rating - 
	title - Link title
	url - Link URL
	target_object - 
	is_external - Information whether the current link is external
	video - Video from link
	"""
	application = None
	button = None
	caption = None
	description = None
	id = None
	is_favorite = None
	photo = None
	preview_page = None
	preview_url = None
	product = None
	rating = None
	title = None
	url = None
	target_object = None
	is_external = None
	video = None


class BaseLinkApplication(BaseModel):
	"""VK Object BaseLinkApplication

	app_id - Application Id
	store - 
	"""
	app_id = None
	store = None


class BaseLinkApplicationStore(BaseModel):
	"""VK Object BaseLinkApplicationStore

	id - Store Id
	name - Store name
	"""
	id = None
	name = None


class BaseLinkButton(BaseModel):
	"""VK Object BaseLinkButton

	action - Button action
	title - Button title
	block_id - Target block id
	section_id - Target section id
	curator_id - curator id
	owner_id - Owner id
	icon - Button icon name, e.g. 'phone' or 'gift'
	style - 
	"""
	action = None
	title = None
	block_id = None
	section_id = None
	curator_id = None
	owner_id = None
	icon = None
	style = None


class BaseLinkButtonAction(BaseModel):
	"""VK Object BaseLinkButtonAction

	type - 
	url - Action URL
	consume_reason - 
	"""
	type = None
	url = None
	consume_reason = None


class BaseLinkButtonActionType(enum.Enum):
	"""VK Object BaseLinkButtonActionType

	"""
	OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
	"""VK Object BaseLinkButtonStyle

	"""
	PRIMARY = "primary"
	SECONDARY = "secondary"


class BaseLinkProduct(BaseModel):
	"""VK Object BaseLinkProduct

	"""
	price = None
	merchant = None
	orders_count = None


class BaseLinkProductStatus(enum.Enum):
	"""VK Object BaseLinkProductStatus

	"""
	ACTIVE = "active"
	BLOCKED = "blocked"
	SOLD = "sold"
	DELETED = "deleted"
	ARCHIVED = "archived"


class BaseLinkRating(BaseModel):
	"""VK Object BaseLinkRating

	reviews_count - Count of reviews
	stars - Count of stars
	"""
	reviews_count = None
	stars = None


class BaseMessageError(BaseModel):
	"""VK Object BaseMessageError

	code - Error code
	description - Error message
	"""
	code = None
	description = None


class BaseOBject(BaseModel):
	"""VK Object BaseOBject

	id - Object ID
	title - Object title
	"""
	id = None
	title = None


class BaseOBjectCount(BaseModel):
	"""VK Object BaseOBjectCount

	count - Items count
	"""
	count = None


class BaseOBjectWithName(BaseModel):
	"""VK Object BaseOBjectWithName

	id - Object ID
	name - Object name
	"""
	id = None
	name = None


class BasePlace(BaseModel):
	"""VK Object BasePlace

	address - Place address
	checkins - Checkins number
	city - City name
	country - Country name
	created - Date of the place creation in Unixtime
	icon - URL of the place's icon
	id - Place ID
	latitude - Place latitude
	longitude - Place longitude
	title - Place title
	type - Place type
	"""
	address = None
	checkins = None
	city = None
	country = None
	created = None
	icon = None
	id = None
	latitude = None
	longitude = None
	title = None
	type = None


class BasePropertyExists(enum.IntEnum):
	"""VK Object BasePropertyExists

	"""
	Property exists = 1


class BaseRepostsInfo(BaseModel):
	"""VK Object BaseRepostsInfo

	count - Total reposts counter. Sum of wall and mail reposts counters
	wall_count - Wall reposts counter
	mail_count - Mail reposts counter
	user_reposted - Information whether current user has reposted the post
	"""
	count = None
	wall_count = None
	mail_count = None
	user_reposted = None


class BaseRequestParam(BaseModel):
	"""VK Object BaseRequestParam

	key - Parameter name
	value - Parameter value
	"""
	key = None
	value = None


class BaseSex(enum.IntEnum):
	"""VK Object BaseSex

	"""
	unknown = 0
	female = 1
	male = 2


class BaseSticker(BaseModel):
	"""VK Object BaseSticker

	sticker_id - Sticker ID
	product_id - Pack ID
	images - 
	images_with_background - 
	animation_url - URL of sticker animation script
	animations - Array of sticker animation script objects
	is_allowed - Information whether the sticker is allowed
	"""
	sticker_id = None
	product_id = None
	images = None
	images_with_background = None
	animation_url = None
	animations = None
	is_allowed = None


class BaseStickerAnimation(BaseModel):
	"""VK Object BaseStickerAnimation

	type - Type of animation script
	url - URL of animation script
	"""
	type = None
	url = None
None

class BaseUploadServer(BaseModel):
	"""VK Object BaseUploadServer

	upload_url - Upload URL
	"""
	upload_url = None


class BaseUserGroupFields(enum.Enum):
	"""VK Object BaseUserGroupFields

	"""
	ABOUT = "about"
	ACTION_BUTTON = "action_button"
	ACTIVITIES = "activities"
	ACTIVITY = "activity"
	ADDRESSES = "addresses"
	ADMIN_LEVEL = "admin_level"
	AGE_LIMITS = "age_limits"
	AUTHOR_ID = "author_id"
	BAN_INFO = "ban_info"
	BDATE = "bdate"
	BLACKLISTED = "blacklisted"
	BLACKLISTED_BY_ME = "blacklisted_by_me"
	BOOKS = "books"
	CAN_CREATE_TOPIC = "can_create_topic"
	CAN_MESSAGE = "can_message"
	CAN_POST = "can_post"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_SEE_AUDIO = "can_see_audio"
	CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
	CAN_UPLOAD_VIDEO = "can_upload_video"
	CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
	CAREER = "career"
	CITY = "city"
	COMMON_COUNT = "common_count"
	CONNECTIONS = "connections"
	CONTACTS = "contacts"
	COUNTERS = "counters"
	COUNTRY = "country"
	COVER = "cover"
	CROP_PHOTO = "crop_photo"
	DEACTIVATED = "deactivated"
	DESCRIPTION = "description"
	DOMAIN = "domain"
	EDUCATION = "education"
	EXPORTS = "exports"
	FINISH_DATE = "finish_date"
	FIXED_POST = "fixed_post"
	FOLLOWERS_COUNT = "followers_count"
	FRIEND_STATUS = "friend_status"
	GAMES = "games"
	HAS_MARKET_APP = "has_market_app"
	HAS_MOBILE = "has_mobile"
	HAS_PHOTO = "has_photo"
	HOME_TOWN = "home_town"
	ID = "id"
	INTERESTS = "interests"
	IS_ADMIN = "is_admin"
	IS_CLOSED = "is_closed"
	IS_FAVORITE = "is_favorite"
	IS_FRIEND = "is_friend"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	IS_MEMBER = "is_member"
	IS_MESSAGES_BLOCKED = "is_messages_blocked"
	CAN_SEND_NOTIFY = "can_send_notify"
	IS_SUBSCRIBED = "is_subscribed"
	LAST_SEEN = "last_seen"
	LINKS = "links"
	LISTS = "lists"
	MAIDEN_NAME = "maiden_name"
	MAIN_ALBUM_ID = "main_album_id"
	MAIN_SECTION = "main_section"
	MARKET = "market"
	MEMBER_STATUS = "member_status"
	MEMBERS_COUNT = "members_count"
	MILITARY = "military"
	MOVIES = "movies"
	MUSIC = "music"
	NAME = "name"
	NICKNAME = "nickname"
	OCCUPATION = "occupation"
	ONLINE = "online"
	ONLINE_STATUS = "online_status"
	PERSONAL = "personal"
	PHONE = "phone"
	PHOTO_100 = "photo_100"
	PHOTO_200 = "photo_200"
	PHOTO_200_ORIG = "photo_200_orig"
	PHOTO_400_ORIG = "photo_400_orig"
	PHOTO_50 = "photo_50"
	PHOTO_ID = "photo_id"
	PHOTO_MAX = "photo_max"
	PHOTO_MAX_ORIG = "photo_max_orig"
	QUOTES = "quotes"
	RELATION = "relation"
	RELATIVES = "relatives"
	SCHOOLS = "schools"
	SCREEN_NAME = "screen_name"
	SEX = "sex"
	SITE = "site"
	START_DATE = "start_date"
	STATUS = "status"
	TIMEZONE = "timezone"
	TRENDING = "trending"
	TV = "tv"
	TYPE = "type"
	UNIVERSITIES = "universities"
	VERIFIED = "verified"
	WALL_COMMENTS = "wall_comments"
	WIKI_PAGE = "wiki_page"
	VK_ADMIN_STATUS = "vk_admin_status"


class BaseUserId(BaseModel):
	"""VK Object BaseUserId

	user_id - User ID
	"""
	user_id = None


class BoardDefaultOrder(enum.IntEnum):
	"""VK Object BoardDefaultOrder

	"""
	desc_updated = 1
	desc_created = 2
	asc_updated = -1
	asc_created = -2


class BoardTopic(BaseModel):
	"""VK Object BoardTopic

	comments - Comments number
	created - Date when the topic has been created in Unixtime
	created_by - Creator ID
	id - Topic ID
	is_closed - Information whether the topic is closed
	is_fixed - Information whether the topic is fixed
	title - Topic title
	updated - Date when the topic has been updated in Unixtime
	updated_by - ID of user who updated the topic
	"""
	comments = None
	created = None
	created_by = None
	id = None
	is_closed = None
	is_fixed = None
	title = None
	updated = None
	updated_by = None


class BoardTopicComment(BaseModel):
	"""VK Object BoardTopicComment

	attachments - 
	date - Date when the comment has been added in Unixtime
	from_id - Author ID
	id - Comment ID
	real_offset - Real position of the comment
	text - Comment text
	can_edit - Information whether current user can edit the comment
	likes - 
	"""
	attachments = None
	date = None
	from_id = None
	id = None
	real_offset = None
	text = None
	can_edit = None
	likes = None


class BoardTopicPoll(BaseModel):
	"""VK Object BoardTopicPoll

	owner_id - Poll owner's ID
	poll_id - Poll ID
	created - Date when poll has been created in Unixtime
	is_closed - Information whether the poll is closed
	question - Poll question
	votes - Votes number
	answer_id - Current user's answer ID
	answers - 
	"""
	owner_id = None
	poll_id = None
	created = None
	is_closed = None
	question = None
	votes = None
	answer_id = None
	answers = None


class CallbaCkBoardPostDelete(BaseModel):
	"""VK Object CallbaCkBoardPostDelete

	"""
	topic_owner_id = None
	topic_id = None
	id = None


class CallbaCkConfirmationMessage(BaseModel):
	"""VK Object CallbaCkConfirmationMessage

	"""
	type = None
	group_id = None
	secret = None


class CallbaCkDonutMoneyWithdraw(BaseModel):
	"""VK Object CallbaCkDonutMoneyWithdraw

	"""
	amount = None
	amount_without_fee = None


class CallbaCkDonutMoneyWithdrawError(BaseModel):
	"""VK Object CallbaCkDonutMoneyWithdrawError

	"""
	reason = None


class CallbaCkDonutSubsCriptionCanCelled(BaseModel):
	"""VK Object CallbaCkDonutSubsCriptionCanCelled

	"""
	user_id = None


class CallbaCkDonutSubsCriptionCreate(BaseModel):
	"""VK Object CallbaCkDonutSubsCriptionCreate

	"""
	user_id = None
	amount = None
	amount_without_fee = None


class CallbaCkDonutSubsCriptionExpired(BaseModel):
	"""VK Object CallbaCkDonutSubsCriptionExpired

	"""
	user_id = None


class CallbaCkDonutSubsCriptionPriCeChanged(BaseModel):
	"""VK Object CallbaCkDonutSubsCriptionPriCeChanged

	"""
	user_id = None
	amount_old = None
	amount_new = None
	amount_diff = None
	amount_diff_without_fee = None


class CallbaCkDonutSubsCriptionProlonged(BaseModel):
	"""VK Object CallbaCkDonutSubsCriptionProlonged

	"""
	user_id = None
	amount = None
	amount_without_fee = None


class CallbaCkGroupChangePhoto(BaseModel):
	"""VK Object CallbaCkGroupChangePhoto

	"""
	user_id = None
	photo = None


class CallbaCkGroupChangeSettings(BaseModel):
	"""VK Object CallbaCkGroupChangeSettings

	"""
	user_id = None
	self = None


class CallbaCkGroupJoin(BaseModel):
	"""VK Object CallbaCkGroupJoin

	"""
	user_id = None
	join_type = None


class CallbaCkGroupJoinType(enum.Enum):
	"""VK Object CallbaCkGroupJoinType

	"""
	JOIN = "join"
	UNSURE = "unsure"
	ACCEPTED = "accepted"
	APPROVED = "approved"
	REQUEST = "request"


class CallbaCkGroupLeave(BaseModel):
	"""VK Object CallbaCkGroupLeave

	"""
	user_id = None
	self = None


class CallbaCkGroupMarket(enum.IntEnum):
	"""VK Object CallbaCkGroupMarket

	"""
	disabled = 0
	open = 1


class CallbaCkGroupOffiCerRole(enum.IntEnum):
	"""VK Object CallbaCkGroupOffiCerRole

	"""
	none = 0
	moderator = 1
	editor = 2
	administrator = 3


class CallbaCkGroupOffiCersEdit(BaseModel):
	"""VK Object CallbaCkGroupOffiCersEdit

	"""
	admin_id = None
	user_id = None
	level_old = None
	level_new = None


class CallbaCkGroupSettingsChanges(BaseModel):
	"""VK Object CallbaCkGroupSettingsChanges

	"""
	title = None
	description = None
	access = None
	screen_name = None
	public_category = None
	public_subcategory = None
	age_limits = None
	website = None
	enable_status_default = None
	enable_audio = None
	enable_video = None
	enable_photo = None
	enable_market = None


class CallbaCkLikeAddRemove(BaseModel):
	"""VK Object CallbaCkLikeAddRemove

	"""
	liker_id = None
	object_type = None
	object_owner_id = None
	object_id = None
	post_id = None
	thread_reply_id = None


class CallbaCkMarketComment(BaseModel):
	"""VK Object CallbaCkMarketComment

	"""
	id = None
	from_id = None
	date = None
	text = None
	market_owner_id = None
	photo_id = None


class CallbaCkMarketCommentDelete(BaseModel):
	"""VK Object CallbaCkMarketCommentDelete

	"""
	owner_id = None
	id = None
	user_id = None
	item_id = None


class CallbaCkMessageAllow(BaseModel):
	"""VK Object CallbaCkMessageAllow

	"""
	user_id = None
	key = None


class CallbaCkMessageBase(BaseModel):
	"""VK Object CallbaCkMessageBase

	"""
	type = None
	object = None
	group_id = None


class CallbaCkMessageDeny(BaseModel):
	"""VK Object CallbaCkMessageDeny

	"""
	user_id = None


class CallbaCkMessageType(enum.Enum):
	"""VK Object CallbaCkMessageType

	"""
	AUDIO_NEW = "audio_new"
	BOARD_POST_NEW = "board_post_new"
	BOARD_POST_EDIT = "board_post_edit"
	BOARD_POST_RESTORE = "board_post_restore"
	BOARD_POST_DELETE = "board_post_delete"
	CONFIRMATION = "confirmation"
	GROUP_LEAVE = "group_leave"
	GROUP_JOIN = "group_join"
	GROUP_CHANGE_PHOTO = "group_change_photo"
	GROUP_CHANGE_SETTINGS = "group_change_settings"
	GROUP_OFFICERS_EDIT = "group_officers_edit"
	LEAD_FORMS_NEW = "lead_forms_new"
	MARKET_COMMENT_NEW = "market_comment_new"
	MARKET_COMMENT_DELETE = "market_comment_delete"
	MARKET_COMMENT_EDIT = "market_comment_edit"
	MARKET_COMMENT_RESTORE = "market_comment_restore"
	MESSAGE_ALLOW = "message_allow"
	MESSAGE_NEW = "message_new"
	MESSAGE_DENY = "message_deny"
	MESSAGE_READ = "message_read"
	MESSAGE_REPLY = "message_reply"
	MESSAGE_EDIT = "message_edit"
	MESSAGE_TYPING_STATE = "message_typing_state"
	MESSAGES_EDIT = "messages_edit"
	PHOTO_NEW = "photo_new"
	PHOTO_COMMENT_NEW = "photo_comment_new"
	PHOTO_COMMENT_DELETE = "photo_comment_delete"
	PHOTO_COMMENT_EDIT = "photo_comment_edit"
	PHOTO_COMMENT_RESTORE = "photo_comment_restore"
	POLL_VOTE_NEW = "poll_vote_new"
	USER_BLOCK = "user_block"
	USER_UNBLOCK = "user_unblock"
	VIDEO_NEW = "video_new"
	VIDEO_COMMENT_NEW = "video_comment_new"
	VIDEO_COMMENT_DELETE = "video_comment_delete"
	VIDEO_COMMENT_EDIT = "video_comment_edit"
	VIDEO_COMMENT_RESTORE = "video_comment_restore"
	WALL_POST_NEW = "wall_post_new"
	WALL_REPLY_NEW = "wall_reply_new"
	WALL_REPLY_EDIT = "wall_reply_edit"
	WALL_REPLY_DELETE = "wall_reply_delete"
	WALL_REPLY_RESTORE = "wall_reply_restore"
	WALL_REPOST = "wall_repost"


class CallbaCkPhotoComment(BaseModel):
	"""VK Object CallbaCkPhotoComment

	"""
	id = None
	from_id = None
	date = None
	text = None
	photo_owner_id = None


class CallbaCkPhotoCommentDelete(BaseModel):
	"""VK Object CallbaCkPhotoCommentDelete

	"""
	id = None
	owner_id = None
	user_id = None
	photo_id = None


class CallbaCkPollVoteNew(BaseModel):
	"""VK Object CallbaCkPollVoteNew

	"""
	owner_id = None
	poll_id = None
	option_id = None
	user_id = None


class CallbaCkQrSCan(BaseModel):
	"""VK Object CallbaCkQrSCan

	"""
	user_id = None
	data = None
	type = None
	subtype = None
	reread = None


class CallbaCkUserBloCk(BaseModel):
	"""VK Object CallbaCkUserBloCk

	"""
	admin_id = None
	user_id = None
	unblock_date = None
	reason = None
	comment = None


class CallbaCkUserUnbloCk(BaseModel):
	"""VK Object CallbaCkUserUnbloCk

	"""
	admin_id = None
	user_id = None
	by_end_date = None


class CallbaCkVideoComment(BaseModel):
	"""VK Object CallbaCkVideoComment

	"""
	id = None
	from_id = None
	date = None
	text = None
	video_owner_id = None


class CallbaCkVideoCommentDelete(BaseModel):
	"""VK Object CallbaCkVideoCommentDelete

	"""
	id = None
	owner_id = None
	user_id = None
	video_id = None


class CallbaCkWallCommentDelete(BaseModel):
	"""VK Object CallbaCkWallCommentDelete

	"""
	owner_id = None
	id = None
	user_id = None
	post_id = None


class CallsCall(BaseModel):
	"""VK Object CallsCall

	duration - Call duration
	initiator_id - Caller initiator
	receiver_id - Caller receiver
	state - 
	time - Timestamp for call
	video - Was this call initiated as video call
	"""
	duration = None
	initiator_id = None
	receiver_id = None
	state = None
	time = None
	video = None


class CallsEndState(enum.Enum):
	"""VK Object CallsEndState

	"""
	CANCELED_BY_INITIATOR = "canceled_by_initiator"
	CANCELED_BY_RECEIVER = "canceled_by_receiver"
	REACHED = "reached"


class CallsPartiCipants(BaseModel):
	"""VK Object CallsPartiCipants

	list - 
	count - Participants count
	"""
	list = None
	count = None


class CommentThread(BaseModel):
	"""VK Object CommentThread

	can_post - Information whether current user can comment the post
	count - Comments number
	groups_can_post - Information whether groups can comment the post
	items - 
	show_reply_button - Information whether recommended to display reply button
	"""
	can_post = None
	count = None
	groups_can_post = None
	items = None
	show_reply_button = None


class DatabaseCity(BaseModel):
	"""VK Object DatabaseCity

	area - Area title
	region - Region title
	important - Information whether the city is included in important cities list
	"""
	area = None
	region = None
	important = None


class DatabaseFaculty(BaseModel):
	"""VK Object DatabaseFaculty

	id - Faculty ID
	title - Faculty title
	"""
	id = None
	title = None


class DatabaseRegion(BaseModel):
	"""VK Object DatabaseRegion

	id - Region ID
	title - Region title
	"""
	id = None
	title = None


class DatabaseSchool(BaseModel):
	"""VK Object DatabaseSchool

	id - School ID
	title - School title
	"""
	id = None
	title = None


class DatabaseStation(BaseModel):
	"""VK Object DatabaseStation

	city_id - City ID
	color - Hex color code without #
	id - Station ID
	name - Station name
	"""
	city_id = None
	color = None
	id = None
	name = None


class DatabaseUniversity(BaseModel):
	"""VK Object DatabaseUniversity

	id - University ID
	title - University title
	"""
	id = None
	title = None


class DocsDoc(BaseModel):
	"""VK Object DocsDoc

	id - Document ID
	owner_id - Document owner ID
	title - Document title
	size - File size in bites
	ext - File extension
	url - File URL
	date - Date when file has been uploaded in Unixtime
	type - Document type
	preview - 
	is_licensed - 
	access_key - Access key for the document
	tags - Document tags
	"""
	id = None
	owner_id = None
	title = None
	size = None
	ext = None
	url = None
	date = None
	type = None
	preview = None
	is_licensed = None
	access_key = None
	tags = None


class DocsDocAttachmentType(enum.Enum):
	"""VK Object DocsDocAttachmentType

	"""
	DOC = "doc"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
	"""VK Object DocsDocPreview

	"""
	audio_msg = None
	graffiti = None
	photo = None
	video = None


class DocsDocPreviewAuDioMsg(BaseModel):
	"""VK Object DocsDocPreviewAuDioMsg

	duration - Audio message duration in seconds
	link_mp3 - MP3 file URL
	link_ogg - OGG file URL
	waveform - 
	"""
	duration = None
	link_mp3 = None
	link_ogg = None
	waveform = None


class DocsDocPreviewGraffiti(BaseModel):
	"""VK Object DocsDocPreviewGraffiti

	src - Graffiti file URL
	width - Graffiti width
	height - Graffiti height
	"""
	src = None
	width = None
	height = None


class DocsDocPreviewPhoto(BaseModel):
	"""VK Object DocsDocPreviewPhoto

	"""
	sizes = None


class DocsDocPreviewPhotoSizes(BaseModel):
	"""VK Object DocsDocPreviewPhotoSizes

	src - URL of the image
	width - Width in px
	height - Height in px
	type - 
	"""
	src = None
	width = None
	height = None
	type = None


class DocsDocPreviewViDeo(BaseModel):
	"""VK Object DocsDocPreviewViDeo

	src - Video URL
	width - Video's width in pixels
	height - Video's height in pixels
	file_size - Video file size in bites
	"""
	src = None
	width = None
	height = None
	file_size = None


class DocsDocTypes(BaseModel):
	"""VK Object DocsDocTypes

	id - Doc type ID
	name - Doc type title
	count - Number of docs
	"""
	id = None
	name = None
	count = None


class DonutDonatorSubscriptionInfo(BaseModel):
	"""VK Object DonutDonatorSubscriptionInfo

	"""
	owner_id = None
	next_payment_date = None
	amount = None
	status = None


class EvEntsEvEntAttach(BaseModel):
	"""VK Object EvEntsEvEntAttach

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	id - event ID
	is_favorite - is favorite
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address = None
	button_text = None
	friends = None
	id = None
	is_favorite = None
	member_status = None
	text = None
	time = None


class FaveBookmark(BaseModel):
	"""VK Object FaveBookmark

	added_date - Timestamp, when this item was bookmarked
	link - 
	post - 
	product - 
	seen - Has user seen this item
	tags - 
	type - Item type
	video - 
	"""
	added_date = None
	link = None
	post = None
	product = None
	seen = None
	tags = None
	type = None
	video = None


class FaveBookmarkType(enum.Enum):
	"""VK Object FaveBookmarkType

	"""
	POST = "post"
	VIDEO = "video"
	PRODUCT = "product"
	ARTICLE = "article"
	LINK = "link"


class FavePage(BaseModel):
	"""VK Object FavePage

	description - Some info about user or group
	group - 
	tags - 
	type - Item type
	updated_date - Timestamp, when this page was bookmarked
	user - 
	"""
	description = None
	group = None
	tags = None
	type = None
	updated_date = None
	user = None


class FavePageType(enum.Enum):
	"""VK Object FavePageType

	"""
	USER = "user"
	GROUP = "group"
	HINTS = "hints"


class FaveTag(BaseModel):
	"""VK Object FaveTag

	id - Tag id
	name - Tag name
	"""
	id = None
	name = None


class FriendsFriendExtendedStatus(BaseModel):
	"""VK Object FriendsFriendExtendedStatus

	is_request_unread - Is friend request from other user unread
	"""
	is_request_unread = None


class FriendsFriendStatus(BaseModel):
	"""VK Object FriendsFriendStatus

	friend_status - 
	sign - MD5 hash for the result validation
	user_id - User ID
	"""
	friend_status = None
	sign = None
	user_id = None


class FriendsFriendStatusStatus(enum.IntEnum):
	"""VK Object FriendsFriendStatusStatus

	"""
	not a friend = 0
	outcoming request = 1
	incoming request = 2
	is friend = 3


class FriendsFriendsList(BaseModel):
	"""VK Object FriendsFriendsList

	id - List ID
	name - List title
	"""
	id = None
	name = None


class FriendsMutualFriend(BaseModel):
	"""VK Object FriendsMutualFriend

	common_count - Total mutual friends number
	common_friends - 
	id - User ID
	"""
	common_count = None
	common_friends = None
	id = None


class FriendsRequests(BaseModel):
	"""VK Object FriendsRequests

	from - ID of the user by whom friend has been suggested
	mutual - 
	user_id - User ID
	"""
	_from = None
	mutual = None
	user_id = None


class FriendsRequestsMutual(BaseModel):
	"""VK Object FriendsRequestsMutual

	count - Total mutual friends number
	users - 
	"""
	count = None
	users = None


class FriendsRequestsXtrMessage(BaseModel):
	"""VK Object FriendsRequestsXtrMessage

	from - ID of the user by whom friend has been suggested
	message - Message sent with a request
	mutual - 
	user_id - User ID
	"""
	_from = None
	message = None
	mutual = None
	user_id = None


class FriendsUserXtrLists(BaseModel):
	"""VK Object FriendsUserXtrLists

	"""
	lists = None


class FriendsUserXtrPhone(BaseModel):
	"""VK Object FriendsUserXtrPhone

	phone - User phone
	"""
	phone = None


class GiftsGift(BaseModel):
	"""VK Object GiftsGift

	date - Date when gist has been sent in Unixtime
	from_id - Gift sender ID
	gift - 
	gift_hash - Hash
	id - Gift ID
	message - Comment text
	privacy - 
	"""
	date = None
	from_id = None
	gift = None
	gift_hash = None
	id = None
	message = None
	privacy = None


class GiftsGiftPrivacy(enum.IntEnum):
	"""VK Object GiftsGiftPrivacy

	"""
	name and message for all = 0
	name for all = 1
	name and message for recipient only = 2


class GiftsLayout(BaseModel):
	"""VK Object GiftsLayout

	id - Gift ID
	thumb_512 - URL of the preview image with 512 px in width
	thumb_256 - URL of the preview image with 256 px in width
	thumb_48 - URL of the preview image with 48 px in width
	thumb_96 - URL of the preview image with 96 px in width
	stickers_product_id - ID of the sticker pack, if the gift is representing one
	is_stickers_style - Information whether gift represents a stickers style
	build_id - ID of the build of constructor gift
	keywords - Keywords used for search
	"""
	id = None
	thumb_512 = None
	thumb_256 = None
	thumb_48 = None
	thumb_96 = None
	stickers_product_id = None
	is_stickers_style = None
	build_id = None
	keywords = None


class GroupsAddress(BaseModel):
	"""VK Object GroupsAddress

	additional_address - Additional address to the place (6 floor, left door)
	address - String address to the place (Nevsky, 28)
	city_id - City id of address
	country_id - Country id of address
	distance - Distance from the point
	id - Address id
	latitude - Address latitude
	longitude - Address longitude
	metro_station_id - Metro id of address
	phone - Address phone
	time_offset - Time offset int minutes from utc time
	timetable - Week timetable for the address
	title - Title of the place (Zinger, etc)
	work_info_status - Status of information about timetable
	"""
	additional_address = None
	address = None
	city_id = None
	country_id = None
	distance = None
	id = None
	latitude = None
	longitude = None
	metro_station_id = None
	phone = None
	time_offset = None
	timetable = None
	title = None
	work_info_status = None


class GroupsAddressTimetable(BaseModel):
	"""VK Object GroupsAddressTimetable

	fri - Timetable for friday
	mon - Timetable for monday
	sat - Timetable for saturday
	sun - Timetable for sunday
	thu - Timetable for thursday
	tue - Timetable for tuesday
	wed - Timetable for wednesday
	"""
	fri = None
	mon = None
	sat = None
	sun = None
	thu = None
	tue = None
	wed = None


class GroupsAddressTimetableDay(BaseModel):
	"""VK Object GroupsAddressTimetableDay

	break_close_time - Close time of the break in minutes
	break_open_time - Start time of the break in minutes
	close_time - Close time in minutes
	open_time - Open time in minutes
	"""
	break_close_time = None
	break_open_time = None
	close_time = None
	open_time = None


class GroupsAddressWorkInfoStatus(enum.Enum):
	"""VK Object GroupsAddressWorkInfoStatus

	"""
	NO_INFORMATION = "no_information"
	TEMPORARILY_CLOSED = "temporarily_closed"
	ALWAYS_OPENED = "always_opened"
	TIMETABLE = "timetable"
	FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
	"""VK Object GroupsAddressesInfo

	is_enabled - Information whether addresses is enabled
	main_address_id - Main address id for group
	"""
	is_enabled = None
	main_address_id = None


class GroupsBanInfo(BaseModel):
	"""VK Object GroupsBanInfo

	admin_id - Administrator ID
	comment - Comment for a ban
	comment_visible - Show comment for user
	is_closed - 
	date - Date when user has been added to blacklist in Unixtime
	end_date - Date when user will be removed from blacklist in Unixtime
	reason - 
	"""
	admin_id = None
	comment = None
	comment_visible = None
	is_closed = None
	date = None
	end_date = None
	reason = None


class GroupsBanInfoReason(enum.IntEnum):
	"""VK Object GroupsBanInfoReason

	"""
	other = 0
	spam = 1
	verbal abuse = 2
	strong language = 3
	flood = 4


class GroupsBannedItem(BaseModel):
	"""VK Object GroupsBannedItem

	"""


class GroupsCallbackServer(BaseModel):
	"""VK Object GroupsCallbackServer

	"""
	id = None
	title = None
	creator_id = None
	url = None
	secret_key = None
	status = None


class GroupsCallbackSettinGs(BaseModel):
	"""VK Object GroupsCallbackSettinGs

	api_version - API version used for the events
	events - 
	"""
	api_version = None
	events = None


class GroupsContactsItem(BaseModel):
	"""VK Object GroupsContactsItem

	user_id - User ID
	desc - Contact description
	phone - Contact phone
	email - Contact email
	"""
	user_id = None
	desc = None
	phone = None
	email = None


class GroupsCountersGroup(BaseModel):
	"""VK Object GroupsCountersGroup

	addresses - Addresses number
	albums - Photo albums number
	audios - Audios number
	audio_playlists - Audio playlists number
	docs - Docs number
	market - Market items number
	photos - Photos number
	topics - Topics number
	videos - Videos number
	"""
	addresses = None
	albums = None
	audios = None
	audio_playlists = None
	docs = None
	market = None
	photos = None
	topics = None
	videos = None


class GroupsCover(BaseModel):
	"""VK Object GroupsCover

	enabled - Information whether cover is enabled
	images - 
	"""
	enabled = None
	images = None


class GroupsFields(enum.Enum):
	"""VK Object GroupsFields

	"""
	MARKET = "market"
	MEMBER_STATUS = "member_status"
	IS_FAVORITE = "is_favorite"
	IS_SUBSCRIBED = "is_subscribed"
	IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
	CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
	CITY = "city"
	COUNTRY = "country"
	VERIFIED = "verified"
	DESCRIPTION = "description"
	WIKI_PAGE = "wiki_page"
	MEMBERS_COUNT = "members_count"
	REQUESTS_COUNT = "requests_count"
	COUNTERS = "counters"
	COVER = "cover"
	CAN_POST = "can_post"
	CAN_SUGGEST = "can_suggest"
	CAN_UPLOAD_STORY = "can_upload_story"
	CAN_UPLOAD_DOC = "can_upload_doc"
	CAN_UPLOAD_VIDEO = "can_upload_video"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_CREATE_TOPIC = "can_create_topic"
	ACTIVITY = "activity"
	FIXED_POST = "fixed_post"
	HAS_PHOTO = "has_photo"
	STATUS = "status"
	MAIN_ALBUM_ID = "main_album_id"
	LINKS = "links"
	CONTACTS = "contacts"
	SITE = "site"
	MAIN_SECTION = "main_section"
	SECONDARY_SECTION = "secondary_section"
	WALL = "wall"
	TRENDING = "trending"
	CAN_MESSAGE = "can_message"
	IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
	IS_MESSAGES_BLOCKED = "is_messages_blocked"
	CAN_SEND_NOTIFY = "can_send_notify"
	HAS_GROUP_CHANNEL = "has_group_channel"
	GROUP_CHANNEL = "group_channel"
	ONLINE_STATUS = "online_status"
	START_DATE = "start_date"
	FINISH_DATE = "finish_date"
	AGE_LIMITS = "age_limits"
	BAN_INFO = "ban_info"
	ACTION_BUTTON = "action_button"
	AUTHOR_ID = "author_id"
	PHONE = "phone"
	HAS_MARKET_APP = "has_market_app"
	ADDRESSES = "addresses"
	LIVE_COVERS = "live_covers"
	IS_ADULT = "is_adult"
	CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
	WARNING_NOTIFICATION = "warning_notification"
	MSG_PUSH_ALLOWED = "msg_push_allowed"
	STORIES_ARCHIVE_COUNT = "stories_archive_count"
	VIDEO_LIVE_LEVEL = "video_live_level"
	VIDEO_LIVE_COUNT = "video_live_count"
	CLIPS_COUNT = "clips_count"
	IS_BUSINESS = "is_business"


class GroupsFilter(enum.Enum):
	"""VK Object GroupsFilter

	"""
	ADMIN = "admin"
	EDITOR = "editor"
	MODER = "moder"
	ADVERTISER = "advertiser"
	GROUPS = "groups"
	PUBLICS = "publics"
	EVENTS = "events"
	HAS_ADDRESSES = "has_addresses"


class GroupsGroup(BaseModel):
	"""VK Object GroupsGroup

	id - Community ID
	name - Community name
	screen_name - Domain of the community page
	is_closed - 
	type - 
	is_admin - Information whether current user is administrator
	admin_level - 
	is_member - Information whether current user is member
	is_advertiser - Information whether current user is advertiser
	start_date - Start date in Unixtime format
	finish_date - Finish date in Unixtime format
	deactivated - Information whether community is banned
	photo_50 - URL of square photo of the community with 50 pixels in width
	photo_100 - URL of square photo of the community with 100 pixels in width
	photo_200 - URL of square photo of the community with 200 pixels in width
	"""
	id = None
	name = None
	screen_name = None
	is_closed = None
	type = None
	is_admin = None
	admin_level = None
	is_member = None
	is_advertiser = None
	start_date = None
	finish_date = None
	deactivated = None
	photo_50 = None
	photo_100 = None
	photo_200 = None


class GroupsGroupAccess(enum.IntEnum):
	"""VK Object GroupsGroupAccess

	"""
	open = 0
	closed = 1
	private = 2


class GroupsGroupAdminLevel(enum.IntEnum):
	"""VK Object GroupsGroupAdminLevel

	"""
	moderator = 1
	editor = 2
	administrator = 3


class GroupsGroupAGeLimits(enum.IntEnum):
	"""VK Object GroupsGroupAGeLimits

	"""
	unlimited = 1
	_16 plus = 2
	_18 plus = 3


class GroupsGroupAttach(BaseModel):
	"""VK Object GroupsGroupAttach

	id - group ID
	text - text of attach
	status - activity or category of group
	size - size of group
	is_favorite - is favorite
	"""
	id = None
	text = None
	status = None
	size = None
	is_favorite = None


class GroupsGroupAudio(enum.IntEnum):
	"""VK Object GroupsGroupAudio

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupBanInfo(BaseModel):
	"""VK Object GroupsGroupBanInfo

	comment - Ban comment
	end_date - End date of ban in Unixtime
	reason - 
	"""
	comment = None
	end_date = None
	reason = None


class GroupsGroupCateGory(BaseModel):
	"""VK Object GroupsGroupCateGory

	id - Category ID
	name - Category name
	subcategories - 
	"""
	id = None
	name = None
	subcategories = None


class GroupsGroupCateGoryFull(BaseModel):
	"""VK Object GroupsGroupCateGoryFull

	id - Category ID
	name - Category name
	page_count - Pages number
	page_previews - 
	subcategories - 
	"""
	id = None
	name = None
	page_count = None
	page_previews = None
	subcategories = None


class GroupsGroupCateGoryType(BaseModel):
	"""VK Object GroupsGroupCateGoryType

	"""
	id = None
	name = None


class GroupsGroupDocs(enum.IntEnum):
	"""VK Object GroupsGroupDocs

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupFull(BaseModel):
	"""VK Object GroupsGroupFull

	market - 
	member_status - Current user's member status
	is_adult - Information whether community is adult
	is_hidden_from_feed - Information whether community is hidden from current user's newsfeed
	is_favorite - Information whether community is in faves
	is_subscribed - Information whether current user is subscribed
	city - 
	country - 
	verified - Information whether community is verified
	description - Community description
	wiki_page - Community's main wiki page title
	members_count - Community members number
	requests_count - The number of incoming requests to the community
	video_live_level - Community level live streams achievements
	video_live_count - Number of community's live streams
	clips_count - Number of community's clips
	counters - 
	cover - 
	can_post - Information whether current user can post on community's wall
	can_suggest - 
	can_upload_story - Information whether current user can upload story
	can_upload_doc - Information whether current user can upload doc
	can_upload_video - Information whether current user can upload video
	can_see_all_posts - Information whether current user can see all posts on community's wall
	can_create_topic - Information whether current user can create topic
	activity - Type of group, start date of event or category of public page
	fixed_post - Fixed post ID
	has_photo - Information whether community has photo
	crop_photo - Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества
	status - Community status
	status_audio - 
	main_album_id - Community's main photo album ID
	links - 
	contacts - 
	wall - Information about wall status in community
	site - Community's website
	main_section - 
	secondary_section - 
	trending - Information whether the community has a "fire" pictogram.
	can_message - Information whether current user can send a message to community
	is_messages_blocked - Information whether community can send a message to current user
	can_send_notify - Information whether community can send notifications by phone number to current user
	online_status - Status of replies in community messages
	invited_by - Inviter ID
	age_limits - Information whether age limit
	ban_info - User ban info
	has_market_app - Information whether community has installed market app
	using_vkpay_market_app - 
	has_group_channel - 
	addresses - Info about addresses in groups
	is_subscribed_podcasts - Information whether current user is subscribed to podcasts
	can_subscribe_podcasts - Owner in whitelist or not
	can_subscribe_posts - Can subscribe to wall
	live_covers - Live covers state
	stories_archive_count - 
	"""
	market = None
	member_status = None
	is_adult = None
	is_hidden_from_feed = None
	is_favorite = None
	is_subscribed = None
	city = None
	country = None
	verified = None
	description = None
	wiki_page = None
	members_count = None
	requests_count = None
	video_live_level = None
	video_live_count = None
	clips_count = None
	counters = None
	cover = None
	can_post = None
	can_suggest = None
	can_upload_story = None
	can_upload_doc = None
	can_upload_video = None
	can_see_all_posts = None
	can_create_topic = None
	activity = None
	fixed_post = None
	has_photo = None
	crop_photo = None
	status = None
	status_audio = None
	main_album_id = None
	links = None
	contacts = None
	wall = None
	site = None
	main_section = None
	secondary_section = None
	trending = None
	can_message = None
	is_messages_blocked = None
	can_send_notify = None
	online_status = None
	invited_by = None
	age_limits = None
	ban_info = None
	has_market_app = None
	using_vkpay_market_app = None
	has_group_channel = None
	addresses = None
	is_subscribed_podcasts = None
	can_subscribe_podcasts = None
	can_subscribe_posts = None
	live_covers = None
	stories_archive_count = None


class GroupsGroupFullAGeLimits(enum.IntEnum):
	"""VK Object GroupsGroupFullAGeLimits

	"""
	no = 1
	over 16 = 2
	over 18 = 3


class GroupsGroupFullMainSection(enum.IntEnum):
	"""VK Object GroupsGroupFullMainSection

	"""
	absent = 0
	photos = 1
	topics = 2
	audio = 3
	video = 4
	market = 5


class GroupsGroupFullMemberStatus(enum.IntEnum):
	"""VK Object GroupsGroupFullMemberStatus

	"""
	not a member = 0
	member = 1
	not sure = 2
	declined = 3
	has sent a request = 4
	invited = 5


class GroupsGroupIsClosed(enum.IntEnum):
	"""VK Object GroupsGroupIsClosed

	"""
	open = 0
	closed = 1
	private = 2


class GroupsGroupLink(BaseModel):
	"""VK Object GroupsGroupLink

	name - Link label
	desc - Link description
	edit_title - Information whether the title can be edited
	id - Link ID
	image_processing - Information whether the image on processing
	url - Link URL
	"""
	name = None
	desc = None
	edit_title = None
	id = None
	image_processing = None
	url = None


class GroupsGroupMarketCurrency(enum.IntEnum):
	"""VK Object GroupsGroupMarketCurrency

	"""
	russian rubles = 643
	ukrainian hryvnia = 980
	kazakh tenge = 398
	euro = 978
	us dollars = 840


class GroupsGroupPhotos(enum.IntEnum):
	"""VK Object GroupsGroupPhotos

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupPublicCateGoryList(BaseModel):
	"""VK Object GroupsGroupPublicCateGoryList

	"""
	id = None
	name = None
	subcategories = None


class GroupsGroupRole(enum.Enum):
	"""VK Object GroupsGroupRole

	"""
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	ADVERTISER = "advertiser"


class GroupsGroupSubject(enum.IntEnum):
	"""VK Object GroupsGroupSubject

	"""
	auto = 1
	activity holidays = 2
	business = 3
	pets = 4
	health = 5
	dating and communication = 6
	games = 7
	it = 8
	cinema = 9
	beauty and fashion = 10
	cooking = 11
	art and culture = 12
	literature = 13
	mobile services and internet = 14
	music = 15
	science and technology = 16
	real estate = 17
	news and media = 18
	security = 19
	education = 20
	home and renovations = 21
	politics = 22
	food = 23
	industry = 24
	travel = 25
	work = 26
	entertainment = 27
	religion = 28
	family = 29
	sports = 30
	insurance = 31
	television = 32
	goods and services = 33
	hobbies = 34
	finance = 35
	photo = 36
	esoterics = 37
	electronics and appliances = 38
	erotic = 39
	humor = 40
	society_humanities = 41
	design and graphics = 42


class GroupsGroupSuGGestedPrivacy(enum.IntEnum):
	"""VK Object GroupsGroupSuGGestedPrivacy

	"""
	none = 0
	all = 1
	subscribers = 2


class GroupsGroupTaG(BaseModel):
	"""VK Object GroupsGroupTaG

	"""
	id = None
	name = None
	color = None
	uses = None


class GroupsGroupTopics(enum.IntEnum):
	"""VK Object GroupsGroupTopics

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupType(enum.Enum):
	"""VK Object GroupsGroupType

	"""
	GROUP = "group"
	PAGE = "page"
	EVENT = "event"


class GroupsGroupVideo(enum.IntEnum):
	"""VK Object GroupsGroupVideo

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupWall(enum.IntEnum):
	"""VK Object GroupsGroupWall

	"""
	disabled = 0
	open = 1
	limited = 2
	closed = 3


class GroupsGroupWiki(enum.IntEnum):
	"""VK Object GroupsGroupWiki

	"""
	disabled = 0
	open = 1
	limited = 2


class GroupsGroupsArray(BaseModel):
	"""VK Object GroupsGroupsArray

	count - Communities number
	items - 
	"""
	count = None
	items = None


class GroupsLinksItem(BaseModel):
	"""VK Object GroupsLinksItem

	desc - Link description
	edit_title - Information whether the link title can be edited
	id - Link ID
	name - Link title
	photo_100 - URL of square image of the link with 100 pixels in width
	photo_50 - URL of square image of the link with 50 pixels in width
	url - Link URL
	"""
	desc = None
	edit_title = None
	id = None
	name = None
	photo_100 = None
	photo_50 = None
	url = None


class GroupsLiveCovers(BaseModel):
	"""VK Object GroupsLiveCovers

	is_enabled - Information whether live covers is enabled
	is_scalable - Information whether live covers photo scaling is enabled
	story_ids - 
	"""
	is_enabled = None
	is_scalable = None
	story_ids = None


class GroupsLonGPollEvents(BaseModel):
	"""VK Object GroupsLonGPollEvents

	"""
	audio_new = None
	board_post_delete = None
	board_post_edit = None
	board_post_new = None
	board_post_restore = None
	group_change_photo = None
	group_change_settings = None
	group_join = None
	group_leave = None
	group_officers_edit = None
	lead_forms_new = None
	market_comment_delete = None
	market_comment_edit = None
	market_comment_new = None
	market_comment_restore = None
	market_order_new = None
	market_order_edit = None
	message_allow = None
	message_deny = None
	message_new = None
	message_read = None
	message_reply = None
	message_typing_state = None
	message_edit = None
	photo_comment_delete = None
	photo_comment_edit = None
	photo_comment_new = None
	photo_comment_restore = None
	photo_new = None
	poll_vote_new = None
	user_block = None
	user_unblock = None
	video_comment_delete = None
	video_comment_edit = None
	video_comment_new = None
	video_comment_restore = None
	video_new = None
	wall_post_new = None
	wall_reply_delete = None
	wall_reply_edit = None
	wall_reply_new = None
	wall_reply_restore = None
	wall_repost = None
	donut_subscription_create = None
	donut_subscription_prolonged = None
	donut_subscription_cancelled = None
	donut_subscription_expired = None
	donut_subscription_price_changed = None
	donut_money_withdraw = None
	donut_money_withdraw_error = None


class GroupsLonGPollServer(BaseModel):
	"""VK Object GroupsLonGPollServer

	key - Long Poll key
	server - Long Poll server address
	ts - Number of the last event
	"""
	key = None
	server = None
	ts = None


class GroupsLonGPollSettinGs(BaseModel):
	"""VK Object GroupsLonGPollSettinGs

	api_version - API version used for the events
	events - 
	is_enabled - Shows whether Long Poll is enabled
	"""
	api_version = None
	events = None
	is_enabled = None


class GroupsMarketInfo(BaseModel):
	"""VK Object GroupsMarketInfo

	contact_id - Contact person ID
	currency - 
	currency_text - Currency name
	enabled - Information whether the market is enabled
	main_album_id - Main market album ID
	price_max - Maximum price
	price_min - Minimum price
	"""
	contact_id = None
	currency = None
	currency_text = None
	enabled = None
	main_album_id = None
	price_max = None
	price_min = None


class GroupsMarketState(enum.Enum):
	"""VK Object GroupsMarketState

	"""
	NONE = "none"
	BASIC = "basic"
	ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
	"""VK Object GroupsMemberRole

	id - User ID
	permissions - 
	role - 
	"""
	id = None
	permissions = None
	role = None


class GroupsMemberRolePermission(enum.Enum):
	"""VK Object GroupsMemberRolePermission

	"""
	ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
	"""VK Object GroupsMemberRoleStatus

	"""
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	CREATOR = "creator"


class GroupsMemberStatus(BaseModel):
	"""VK Object GroupsMemberStatus

	member - Information whether user is a member of the group
	user_id - User ID
	"""
	member = None
	user_id = None


class GroupsMemberStatusFull(BaseModel):
	"""VK Object GroupsMemberStatusFull

	can_invite - Information whether user can be invited
	can_recall - Information whether user's invite to the group can be recalled
	invitation - Information whether user has been invited to the group
	member - Information whether user is a member of the group
	request - Information whether user has send request to the group
	user_id - User ID
	"""
	can_invite = None
	can_recall = None
	invitation = None
	member = None
	request = None
	user_id = None


class GroupsOnlineStatus(BaseModel):
	"""VK Object GroupsOnlineStatus

	minutes - Estimated time of answer (for status = answer_mark)
	status - 
	"""
	minutes = None
	status = None


class GroupsOnlineStatusType(enum.Enum):
	"""VK Object GroupsOnlineStatusType

	"""
	NONE = "none"
	ONLINE = "online"
	ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(BaseModel):
	"""VK Object GroupsOwnerXtrBanInfo

	ban_info - 
	group - Information about group if type = group
	profile - Information about group if type = profile
	type - 
	"""
	ban_info = None
	group = None
	profile = None
	type = None


class GroupsOwnerXtrBanInfoType(enum.Enum):
	"""VK Object GroupsOwnerXtrBanInfoType

	"""
	GROUP = "group"
	PROFILE = "profile"


class GroupsProfileItem(BaseModel):
	"""VK Object GroupsProfileItem

	id - User id
	photo_50 - Url for user photo
	photo_100 - Url for user photo
	first_name - User first name
	"""
	id = None
	photo_50 = None
	photo_100 = None
	first_name = None


class GroupsRoleOptions(enum.Enum):
	"""VK Object GroupsRoleOptions

	"""
	MODERATOR = "moderator"
	EDITOR = "editor"
	ADMINISTRATOR = "administrator"
	CREATOR = "creator"


class GroupsSettinGsTwitter(BaseModel):
	"""VK Object GroupsSettinGsTwitter

	"""
	status = None
	name = None


class GroupsSubjectItem(BaseModel):
	"""VK Object GroupsSubjectItem

	id - Subject ID
	name - Subject title
	"""
	id = None
	name = None


class GroupsTokenPermissionSettinG(BaseModel):
	"""VK Object GroupsTokenPermissionSettinG

	"""
	name = None
	setting = None


class GroupsUserXtrRole(BaseModel):
	"""VK Object GroupsUserXtrRole

	"""
	role = None


class LikesType(enum.Enum):
	"""VK Object LikesType

	"""
	POST = "post"
	COMMENT = "comment"
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	NOTE = "note"
	MARKET = "market"
	PHOTO_COMMENT = "photo_comment"
	VIDEO_COMMENT = "video_comment"
	TOPIC_COMMENT = "topic_comment"
	MARKET_COMMENT = "market_comment"
	SITEPAGE = "sitepage"


class LinkTargetObject(BaseModel):
	"""VK Object LinkTargetObject

	type - Object type
	owner_id - Owner ID
	item_id - Item ID
	"""
	type = None
	owner_id = None
	item_id = None


class MarketCurrency(BaseModel):
	"""VK Object MarketCurrency

	id - Currency ID
	name - Currency sign
	"""
	id = None
	name = None


class MarketMarketAlbuM(BaseModel):
	"""VK Object MarketMarketAlbuM

	count - Items number
	id - Market album ID
	owner_id - Market album owner's ID
	photo - 
	title - Market album title
	updated_time - Date when album has been updated last time in Unixtime
	"""
	count = None
	id = None
	owner_id = None
	photo = None
	title = None
	updated_time = None


class MarketMarketCategory(BaseModel):
	"""VK Object MarketMarketCategory

	"""


class MarketMarketCategoryNested(BaseModel):
	"""VK Object MarketMarketCategoryNested

	id - Category ID
	name - Category name
	parent - 
	"""
	id = None
	name = None
	parent = None


class MarketMarketCategoryOld(BaseModel):
	"""VK Object MarketMarketCategoryOld

	id - Category ID
	name - Category name
	section - 
	"""
	id = None
	name = None
	section = None


class MarketMarketCategoryTree(BaseModel):
	"""VK Object MarketMarketCategoryTree

	id - Category ID
	name - Category name
	children - 
	"""
	id = None
	name = None
	children = None


class MarketMarketIteM(BaseModel):
	"""VK Object MarketMarketIteM

	access_key - Access key for the market item
	availability - 
	button_title - Title for button for url
	category - 
	date - Date when the item has been created in Unixtime
	description - Item description
	external_id - 
	id - Item ID
	is_favorite - 
	owner_id - Item owner's ID
	price - 
	thumb_photo - URL of the preview image
	title - Item title
	url - URL to item
	variants_grouping_id - 
	is_main_variant - 
	"""
	access_key = None
	availability = None
	button_title = None
	category = None
	date = None
	description = None
	external_id = None
	id = None
	is_favorite = None
	owner_id = None
	price = None
	thumb_photo = None
	title = None
	url = None
	variants_grouping_id = None
	is_main_variant = None


class MarketMarketIteMAvailability(enum.IntEnum):
	"""VK Object MarketMarketIteMAvailability

	"""
	available = 0
	removed = 1
	unavailable = 2


class MarketMarketIteMFull(BaseModel):
	"""VK Object MarketMarketIteMFull

	albums_ids - 
	photos - 
	can_comment - Information whether current use can comment the item
	can_repost - Information whether current use can repost the item
	likes - 
	reposts - 
	views_count - Views number
	wishlist_item_id - Object identifier in wishlist of viewer
	cancel_info - Information for cancel and revert order
	user_agreement_info - User agreement info
	"""
	albums_ids = None
	photos = None
	can_comment = None
	can_repost = None
	likes = None
	reposts = None
	views_count = None
	wishlist_item_id = None
	cancel_info = None
	user_agreement_info = None


class MarketOrder(BaseModel):
	"""VK Object MarketOrder

	id - 
	group_id - 
	user_id - 
	display_order_id - 
	date - 
	status - 
	items_count - 
	track_number - 
	track_link - 
	comment - 
	address - 
	merchant_comment - 
	weight - 
	total_price - 
	preview_order_items - Several order items for preview
	cancel_info - Information for cancel and revert order
	"""
	id = None
	group_id = None
	user_id = None
	display_order_id = None
	date = None
	status = None
	items_count = None
	track_number = None
	track_link = None
	comment = None
	address = None
	merchant_comment = None
	weight = None
	total_price = None
	preview_order_items = None
	cancel_info = None


class MarketOrderIteM(BaseModel):
	"""VK Object MarketOrderIteM

	"""
	owner_id = None
	item_id = None
	price = None
	quantity = None
	item = None
	title = None
	photo = None
	variants = None


class MarketPrice(BaseModel):
	"""VK Object MarketPrice

	amount - Amount
	currency - 
	discount_rate - 
	old_amount - 
	text - Text
	old_amount_text - Textual representation of old price
	"""
	amount = None
	currency = None
	discount_rate = None
	old_amount = None
	text = None
	old_amount_text = None


class MarketSection(BaseModel):
	"""VK Object MarketSection

	id - Section ID
	name - Section name
	"""
	id = None
	name = None


class MediaRestriction(BaseModel):
	"""VK Object MediaRestriction

	text - 
	title - 
	button - 
	always_shown - Need show restriction always or not
	blur - Need blur current video or not
	can_play - Can play video or not
	can_preview - Can preview video or not
	card_icon - 
	list_icon - 
	"""
	text = None
	title = None
	button = None
	always_shown = None
	blur = None
	can_play = None
	can_preview = None
	card_icon = None
	list_icon = None


class MessagesAudioMessage(BaseModel):
	"""VK Object MessagesAudioMessage

	access_key - Access key for audio message
	transcript_error - 
	duration - Audio message duration in seconds
	id - Audio message ID
	link_mp3 - MP3 file URL
	link_ogg - OGG file URL
	owner_id - Audio message owner ID
	waveform - 
	"""
	access_key = None
	transcript_error = None
	duration = None
	id = None
	link_mp3 = None
	link_ogg = None
	owner_id = None
	waveform = None


class MessagesChat(BaseModel):
	"""VK Object MessagesChat

	admin_id - Chat creator ID
	id - Chat ID
	kicked - Shows that user has been kicked from the chat
	left - Shows that user has been left the chat
	photo_100 - URL of the preview image with 100 px in width
	photo_200 - URL of the preview image with 200 px in width
	photo_50 - URL of the preview image with 50 px in width
	push_settings - 
	title - Chat title
	type - Chat type
	users - 
	is_default_photo - If provided photo is default
	"""
	admin_id = None
	id = None
	kicked = None
	left = None
	photo_100 = None
	photo_200 = None
	photo_50 = None
	push_settings = None
	title = None
	type = None
	users = None
	is_default_photo = None


class MessagesChatFull(BaseModel):
	"""VK Object MessagesChatFull

	admin_id - Chat creator ID
	id - Chat ID
	kicked - Shows that user has been kicked from the chat
	left - Shows that user has been left the chat
	photo_100 - URL of the preview image with 100 px in width
	photo_200 - URL of the preview image with 200 px in width
	photo_50 - URL of the preview image with 50 px in width
	push_settings - 
	title - Chat title
	type - Chat type
	users - 
	"""
	admin_id = None
	id = None
	kicked = None
	left = None
	photo_100 = None
	photo_200 = None
	photo_50 = None
	push_settings = None
	title = None
	type = None
	users = None


class MessagesChatPreview(BaseModel):
	"""VK Object MessagesChatPreview

	"""
	admin_id = None
	joined = None
	local_id = None
	members = None
	members_count = None
	title = None
	is_member = None


class MessagesChatPushSettings(BaseModel):
	"""VK Object MessagesChatPushSettings

	disabled_until - Time until that notifications are disabled
	sound - Information whether the sound is on
	"""
	disabled_until = None
	sound = None


class MessagesChatRestrictions(BaseModel):
	"""VK Object MessagesChatRestrictions

	admins_promote_users - Only admins can promote users to admins
	only_admins_edit_info - Only admins can change chat info
	only_admins_edit_pin - Only admins can edit pinned message
	only_admins_invite - Only admins can invite users to this chat
	only_admins_kick - Only admins can kick users from this chat
	"""
	admins_promote_users = None
	only_admins_edit_info = None
	only_admins_edit_pin = None
	only_admins_invite = None
	only_admins_kick = None


class MessagesChatSettings(BaseModel):
	"""VK Object MessagesChatSettings

	members_count - 
	friends_count - 
	owner_id - 
	title - Chat title
	pinned_message - 
	state - 
	photo - 
	admin_ids - Ids of chat admins
	active_ids - 
	is_group_channel - 
	acl - 
	permissions - 
	is_disappearing - 
	theme - 
	disappearing_chat_link - 
	is_service - 
	"""
	members_count = None
	friends_count = None
	owner_id = None
	title = None
	pinned_message = None
	state = None
	photo = None
	admin_ids = None
	active_ids = None
	is_group_channel = None
	acl = None
	permissions = None
	is_disappearing = None
	theme = None
	disappearing_chat_link = None
	is_service = None


class MessagesChatSettingsAcl(BaseModel):
	"""VK Object MessagesChatSettingsAcl

	can_change_info - Can you change photo, description and name
	can_change_invite_link - Can you change invite link for this chat
	can_change_pin - Can you pin/unpin message for this chat
	can_invite - Can you invite other peers in chat
	can_promote_users - Can you promote simple users to chat admins
	can_see_invite_link - Can you see invite link for this chat
	can_moderate - Can you moderate (delete) other users' messages
	can_copy_chat - Can you copy chat
	can_call - Can you init group call in the chat
	can_use_mass_mentions - Can you use mass mentions
	can_change_service_type - Can you change chat service type
	"""
	can_change_info = None
	can_change_invite_link = None
	can_change_pin = None
	can_invite = None
	can_promote_users = None
	can_see_invite_link = None
	can_moderate = None
	can_copy_chat = None
	can_call = None
	can_use_mass_mentions = None
	can_change_service_type = None


class MessagesChatSettingsPerMissions(BaseModel):
	"""VK Object MessagesChatSettingsPerMissions

	invite - Who can invite users to chat
	change_info - Who can change chat info
	change_pin - Who can change pinned message
	use_mass_mentions - Who can use mass mentions
	see_invite_link - Who can see invite link
	call - Who can make calls
	change_admins - Who can change admins
	"""
	invite = None
	change_info = None
	change_pin = None
	use_mass_mentions = None
	see_invite_link = None
	call = None
	change_admins = None


class MessagesChatSettingsPhoto(BaseModel):
	"""VK Object MessagesChatSettingsPhoto

	photo_50 - URL of the preview image with 50px in width
	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	is_default_photo - If provided photo is default
	"""
	photo_50 = None
	photo_100 = None
	photo_200 = None
	is_default_photo = None


class MessagesChatSettingsState(enum.Enum):
	"""VK Object MessagesChatSettingsState

	"""
	IN = "in"
	KICKED = "kicked"
	LEFT = "left"


class MessagesConversation(BaseModel):
	"""VK Object MessagesConversation

	peer - 
	sort_id - 
	last_message_id - ID of the last message in conversation
	in_read - Last message user have read
	out_read - Last outcoming message have been read by the opponent
	unread_count - Unread messages number
	is_marked_unread - Is this conversation uread
	out_read_by - 
	important - 
	unanswered - 
	special_service_type - 
	message_request_data - 
	mentions - Ids of messages with mentions
	current_keyboard - 
	push_settings - 
	can_write - 
	chat_settings - 
	"""
	peer = None
	sort_id = None
	last_message_id = None
	in_read = None
	out_read = None
	unread_count = None
	is_marked_unread = None
	out_read_by = None
	important = None
	unanswered = None
	special_service_type = None
	message_request_data = None
	mentions = None
	current_keyboard = None
	push_settings = None
	can_write = None
	chat_settings = None


class MessagesConversationCanWrite(BaseModel):
	"""VK Object MessagesConversationCanWrite

	"""
	allowed = None
	reason = None


class MessagesConversationMeMber(BaseModel):
	"""VK Object MessagesConversationMeMber

	can_kick - Is it possible for user to kick this member
	invited_by - 
	is_admin - 
	is_owner - 
	is_message_request - 
	join_date - 
	request_date - Message request date
	member_id - 
	"""
	can_kick = None
	invited_by = None
	is_admin = None
	is_owner = None
	is_message_request = None
	join_date = None
	request_date = None
	member_id = None


class MessagesConversationPeer(BaseModel):
	"""VK Object MessagesConversationPeer

	"""
	id = None
	local_id = None
	type = None


class MessagesConversationPeerType(enum.Enum):
	"""VK Object MessagesConversationPeerType

	"""
	CHAT = "chat"
	EMAIL = "email"
	USER = "user"
	GROUP = "group"


class MessagesConversationSortId(BaseModel):
	"""VK Object MessagesConversationSortId

	major_id - Major id for sorting conversations
	minor_id - Minor id for sorting conversations
	"""
	major_id = None
	minor_id = None


class MessagesConversationWithMessage(BaseModel):
	"""VK Object MessagesConversationWithMessage

	"""
	conversation = None
	last_message = None


class MessagesForeignMessage(BaseModel):
	"""VK Object MessagesForeignMessage

	attachments - 
	conversation_message_id - Conversation message ID
	date - Date when the message was created
	from_id - Message author's ID
	fwd_messages - 
	geo - 
	id - Message ID
	peer_id - Peer ID
	reply_message - 
	text - Message text
	update_time - Date when the message has been updated in Unixtime
	was_listened - Was the audio message inside already listened by you
	payload - Additional data sent along with message for developer convenience
	"""
	attachments = None
	conversation_message_id = None
	date = None
	from_id = None
	fwd_messages = None
	geo = None
	id = None
	peer_id = None
	reply_message = None
	text = None
	update_time = None
	was_listened = None
	payload = None


class MessagesForward(BaseModel):
	"""VK Object MessagesForward

	owner_id - Messages owner_id
	peer_id - Messages peer_id
	conversation_message_ids - 
	message_ids - 
	is_reply - If you need to reply to a message
	"""
	owner_id = None
	peer_id = None
	conversation_message_ids = None
	message_ids = None
	is_reply = None


class MessagesGraffiti(BaseModel):
	"""VK Object MessagesGraffiti

	access_key - Access key for graffiti
	height - Graffiti height
	id - Graffiti ID
	owner_id - Graffiti owner ID
	url - Graffiti URL
	width - Graffiti width
	"""
	access_key = None
	height = None
	id = None
	owner_id = None
	url = None
	width = None


class MessagesHistoryAttachMent(BaseModel):
	"""VK Object MessagesHistoryAttachMent

	attachment - 
	message_id - Message ID
	from_id - Message author's ID
	forward_level - Forward level (optional)
	"""
	attachment = None
	message_id = None
	from_id = None
	forward_level = None


class MessagesHistoryMessageAttachMent(BaseModel):
	"""VK Object MessagesHistoryMessageAttachMent

	"""
	audio = None
	audio_message = None
	doc = None
	graffiti = None
	link = None
	market = None
	photo = None
	share = None
	type = None
	video = None
	wall = None


class MessagesHistoryMessageAttachMentType(enum.Enum):
	"""VK Object MessagesHistoryMessageAttachMentType

	"""
	PHOTO = "photo"
	VIDEO = "video"
	AUDIO = "audio"
	DOC = "doc"
	LINK = "link"
	MARKET = "market"
	WALL = "wall"
	SHARE = "share"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(BaseModel):
	"""VK Object MessagesKeyboard

	author_id - Community or bot, which set this keyboard
	buttons - 
	one_time - Should this keyboard disappear on first use
	inline - 
	"""
	author_id = None
	buttons = None
	one_time = None
	inline = None


class MessagesKeyboardButton(BaseModel):
	"""VK Object MessagesKeyboardButton

	action - 
	color - Button color
	"""
	action = None
	color = None


class MessagesKeyboardButtonAction(BaseModel):
	"""VK Object MessagesKeyboardButtonAction

	app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
	hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
	label - Label for button
	link - link for button
	owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
	payload - Additional data sent along with message for developer convenience
	type - Button type
	"""
	app_id = None
	hash = None
	label = None
	link = None
	owner_id = None
	payload = None
	type = None


class MessagesLastActivity(BaseModel):
	"""VK Object MessagesLastActivity

	online - Information whether user is online
	time - Time when user was online in Unixtime
	"""
	online = None
	time = None


class MessagesLongpollMessages(BaseModel):
	"""VK Object MessagesLongpollMessages

	count - Total number
	items - 
	"""
	count = None
	items = None


class MessagesLongpollParaMs(BaseModel):
	"""VK Object MessagesLongpollParaMs

	server - Server URL
	key - Key
	ts - Timestamp
	pts - Persistent timestamp
	"""
	server = None
	key = None
	ts = None
	pts = None


class MessagesMessage(BaseModel):
	"""VK Object MessagesMessage

	action - 
	admin_author_id - Only for messages from community. Contains user ID of community admin, who sent this message.
	attachments - 
	conversation_message_id - Unique auto-incremented number for all messages with this peer
	date - Date when the message has been sent in Unixtime
	deleted - Is it an deleted message
	from_id - Message author's ID
	fwd_messages - Forwarded messages
	geo - 
	id - Message ID
	important - Is it an important message
	is_hidden - 
	is_cropped - this message is cropped for bot
	keyboard - 
	members_count - Members number
	out - Information whether the message is outcoming
	payload - 
	peer_id - Peer ID
	random_id - ID used for sending messages. It returned only for outgoing messages
	ref - 
	ref_source - 
	reply_message - 
	text - Message text
	update_time - Date when the message has been updated in Unixtime
	was_listened - Was the audio message inside already listened by you
	pinned_at - Date when the message has been pinned in Unixtime
	"""
	action = None
	admin_author_id = None
	attachments = None
	conversation_message_id = None
	date = None
	deleted = None
	from_id = None
	fwd_messages = None
	geo = None
	id = None
	important = None
	is_hidden = None
	is_cropped = None
	keyboard = None
	members_count = None
	out = None
	payload = None
	peer_id = None
	random_id = None
	ref = None
	ref_source = None
	reply_message = None
	text = None
	update_time = None
	was_listened = None
	pinned_at = None


class MessagesMessageAction(BaseModel):
	"""VK Object MessagesMessageAction

	conversation_message_id - Message ID
	email - Email address for chat_invite_user or chat_kick_user actions
	member_id - User or email peer ID
	message - Message body of related message
	photo - 
	text - New chat title for chat_create and chat_title_update actions
	type - 
	"""
	conversation_message_id = None
	email = None
	member_id = None
	message = None
	photo = None
	text = None
	type = None


class MessagesMessageActionPhoto(BaseModel):
	"""VK Object MessagesMessageActionPhoto

	photo_100 - URL of the preview image with 100px in width
	photo_200 - URL of the preview image with 200px in width
	photo_50 - URL of the preview image with 50px in width
	"""
	photo_100 = None
	photo_200 = None
	photo_50 = None


class MessagesMessageActionStatus(enum.Enum):
	"""VK Object MessagesMessageActionStatus

	"""
	CHAT_PHOTO_UPDATE = "chat_photo_update"
	CHAT_PHOTO_REMOVE = "chat_photo_remove"
	CHAT_CREATE = "chat_create"
	CHAT_TITLE_UPDATE = "chat_title_update"
	CHAT_INVITE_USER = "chat_invite_user"
	CHAT_KICK_USER = "chat_kick_user"
	CHAT_PIN_MESSAGE = "chat_pin_message"
	CHAT_UNPIN_MESSAGE = "chat_unpin_message"
	CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"


class MessagesMessageAttachMent(BaseModel):
	"""VK Object MessagesMessageAttachMent

	"""
	audio = None
	audio_message = None
	call = None
	doc = None
	gift = None
	graffiti = None
	link = None
	market = None
	market_market_album = None
	photo = None
	sticker = None
	story = None
	type = None
	video = None
	wall = None
	wall_reply = None
	poll = None


class MessagesMessageAttachMentType(enum.Enum):
	"""VK Object MessagesMessageAttachMentType

	"""
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	MARKET = "market"
	MARKET_ALBUM = "market_album"
	GIFT = "gift"
	STICKER = "sticker"
	WALL = "wall"
	WALL_REPLY = "wall_reply"
	ARTICLE = "article"
	POLL = "poll"
	CALL = "call"
	GRAFFITI = "graffiti"
	AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(BaseModel):
	"""VK Object MessagesMessageRequestData

	status - Status of message request
	inviter_id - Message request sender id
	request_date - Message request date
	"""
	status = None
	inviter_id = None
	request_date = None


class MessagesMessagesArray(BaseModel):
	"""VK Object MessagesMessagesArray

	"""
	count = None
	items = None


class MessagesOutReadBy(BaseModel):
	"""VK Object MessagesOutReadBy

	"""
	count = None
	member_ids = None


class MessagesPinnedMessage(BaseModel):
	"""VK Object MessagesPinnedMessage

	attachments - 
	conversation_message_id - Unique auto-incremented number for all messages with this peer
	date - Date when the message has been sent in Unixtime
	from_id - Message author's ID
	fwd_messages - Forwarded messages
	geo - 
	id - Message ID
	peer_id - Peer ID
	reply_message - 
	text - Message text
	keyboard - 
	"""
	attachments = None
	conversation_message_id = None
	date = None
	from_id = None
	fwd_messages = None
	geo = None
	id = None
	peer_id = None
	reply_message = None
	text = None
	keyboard = None


class MessagesPushSettings(BaseModel):
	"""VK Object MessagesPushSettings

	disabled_forever - Information whether push notifications are disabled forever
	disabled_until - Time until what notifications are disabled
	no_sound - Information whether the sound is on
	"""
	disabled_forever = None
	disabled_until = None
	no_sound = None


class MessagesTeMplateActionTypeNaMes(enum.Enum):
	"""VK Object MessagesTeMplateActionTypeNaMes

	"""
	TEXT = "text"
	START = "start"
	LOCATION = "location"
	VKPAY = "vkpay"
	OPEN_APP = "open_app"
	OPEN_PHOTO = "open_photo"
	OPEN_LINK = "open_link"
	CALLBACK = "callback"


class MessagesUserXtrInvitedBy(BaseModel):
	"""VK Object MessagesUserXtrInvitedBy

	invited_by - ID of the inviter
	"""
	invited_by = None


class NewsfeedCommeNtsFilters(enum.Enum):
	"""VK Object NewsfeedCommeNtsFilters

	"""
	POST = "post"
	PHOTO = "photo"
	VIDEO = "video"
	TOPIC = "topic"
	NOTE = "note"


class NewsfeedEveNtActivity(BaseModel):
	"""VK Object NewsfeedEveNtActivity

	address - address of event
	button_text - text of attach
	friends - array of friends ids
	member_status - Current user's member status
	text - text of attach
	time - event start time
	"""
	address = None
	button_text = None
	friends = None
	member_status = None
	text = None
	time = None


class NewsfeedFilters(enum.Enum):
	"""VK Object NewsfeedFilters

	"""
	POST = "post"
	PHOTO = "photo"
	PHOTO_TAG = "photo_tag"
	WALL_PHOTO = "wall_photo"
	FRIEND = "friend"
	NOTE = "note"
	AUDIO = "audio"
	VIDEO = "video"
	AUDIO_PLAYLIST = "audio_playlist"
	CLIP = "clip"


class NewsfeedIgNoreItemType(enum.Enum):
	"""VK Object NewsfeedIgNoreItemType

	"""
	WALL = "wall"
	TAG = "tag"
	PROFILEPHOTO = "profilephoto"
	VIDEO = "video"
	PHOTO = "photo"
	AUDIO = "audio"


class NewsfeedItemAudio(BaseModel):
	"""VK Object NewsfeedItemAudio

	audio - 
	post_id - Post ID
	"""
	audio = None
	post_id = None


class NewsfeedItemAudioAudio(BaseModel):
	"""VK Object NewsfeedItemAudioAudio

	count - Audios number
	items - 
	"""
	count = None
	items = None


class NewsfeedItemBase(BaseModel):
	"""VK Object NewsfeedItemBase

	type - 
	source_id - Item source ID
	date - Date when item has been added in Unixtime
	"""
	type = None
	source_id = None
	date = None


class NewsfeedItemDigest(BaseModel):
	"""VK Object NewsfeedItemDigest

	feed_id - id of feed in digest
	items - 
	main_post_ids - 
	template - type of digest
	header - 
	footer - 
	track_code - 
	"""
	feed_id = None
	items = None
	main_post_ids = None
	template = None
	header = None
	footer = None
	track_code = None


class NewsfeedItemDigestButtoN(BaseModel):
	"""VK Object NewsfeedItemDigestButtoN

	"""
	title = None
	style = None


class NewsfeedItemDigestFooter(BaseModel):
	"""VK Object NewsfeedItemDigestFooter

	style - 
	text - text for invite to enable smart feed
	button - 
	"""
	style = None
	text = None
	button = None


class NewsfeedItemDigestFullItem(BaseModel):
	"""VK Object NewsfeedItemDigestFullItem

	"""
	text = None
	source_name = None
	attachment_index = None
	attachment = None
	style = None
	post = None


class NewsfeedItemDigestHeader(BaseModel):
	"""VK Object NewsfeedItemDigestHeader

	title - Title of the header
	subtitle - Subtitle of the header, when title have two strings
	style - 
	button - 
	"""
	title = None
	subtitle = None
	style = None
	button = None


class NewsfeedItemDigestItem(BaseModel):
	"""VK Object NewsfeedItemDigestItem

	"""


class NewsfeedItemFrieNd(BaseModel):
	"""VK Object NewsfeedItemFrieNd

	"""
	friends = None


class NewsfeedItemFrieNdFrieNds(BaseModel):
	"""VK Object NewsfeedItemFrieNdFrieNds

	count - Number of friends has been added
	items - 
	"""
	count = None
	items = None


class NewsfeedItemHolidayRecommeNdatioNsBlockHeader(BaseModel):
	"""VK Object NewsfeedItemHolidayRecommeNdatioNsBlockHeader

	title - Title of the header
	subtitle - Subtitle of the header
	image - 
	action - 
	"""
	title = None
	subtitle = None
	image = None
	action = None


class NewsfeedItemPhoto(BaseModel):
	"""VK Object NewsfeedItemPhoto

	photos - 
	post_id - Post ID
	"""
	photos = None
	post_id = None


class NewsfeedItemPhotoPhotos(BaseModel):
	"""VK Object NewsfeedItemPhotoPhotos

	count - Photos number
	items - 
	"""
	count = None
	items = None


class NewsfeedItemPhotoTag(BaseModel):
	"""VK Object NewsfeedItemPhotoTag

	photo_tags - 
	post_id - Post ID
	"""
	photo_tags = None
	post_id = None


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
	"""VK Object NewsfeedItemPhotoTagPhotoTags

	count - Tags number
	items - 
	"""
	count = None
	items = None


class NewsfeedItemPromoButtoN(BaseModel):
	"""VK Object NewsfeedItemPromoButtoN

	"""
	text = None
	title = None
	action = None
	images = None
	track_code = None


class NewsfeedItemPromoButtoNActioN(BaseModel):
	"""VK Object NewsfeedItemPromoButtoNActioN

	"""
	url = None
	type = None
	target = None


class NewsfeedItemPromoButtoNImage(BaseModel):
	"""VK Object NewsfeedItemPromoButtoNImage

	"""
	width = None
	height = None
	url = None


class NewsfeedItemTopic(BaseModel):
	"""VK Object NewsfeedItemTopic

	comments - 
	likes - 
	post_id - Topic post ID
	text - Post text
	"""
	comments = None
	likes = None
	post_id = None
	text = None


class NewsfeedItemVideo(BaseModel):
	"""VK Object NewsfeedItemVideo

	"""
	video = None


class NewsfeedItemVideoVideo(BaseModel):
	"""VK Object NewsfeedItemVideoVideo

	count - Tags number
	items - 
	"""
	count = None
	items = None


class NewsfeedItemWallpost(BaseModel):
	"""VK Object NewsfeedItemWallpost

	activity - 
	attachments - 
	comments - 
	copy_history - 
	feedback - 
	geo - 
	is_favorite - Information whether the post in favorites list
	likes - 
	marked_as_ads - Information whether the post is marked as ads
	post_id - Post ID
	post_source - 
	post_type - 
	reposts - 
	signer_id - Post signer ID
	text - Post text
	views - Count of views
	short_text_rate - Preview length control parameter
	"""
	activity = None
	attachments = None
	comments = None
	copy_history = None
	feedback = None
	geo = None
	is_favorite = None
	likes = None
	marked_as_ads = None
	post_id = None
	post_source = None
	post_type = None
	reposts = None
	signer_id = None
	text = None
	views = None
	short_text_rate = None


class NewsfeedItemWallpostFeedback(BaseModel):
	"""VK Object NewsfeedItemWallpostFeedback

	"""
	type = None
	question = None
	answers = None
	stars_count = None
	gratitude = None


class NewsfeedItemWallpostFeedbackANswer(BaseModel):
	"""VK Object NewsfeedItemWallpostFeedbackANswer

	"""
	title = None
	id = None


class NewsfeedItemWallpostFeedbackType(enum.Enum):
	"""VK Object NewsfeedItemWallpostFeedbackType

	"""
	BUTTONS = "buttons"
	STARS = "stars"


class NewsfeedItemWallpostType(enum.Enum):
	"""VK Object NewsfeedItemWallpostType

	"""
	POST = "post"
	COPY = "copy"
	REPLY = "reply"


class NewsfeedList(BaseModel):
	"""VK Object NewsfeedList

	id - List ID
	title - List title
	"""
	id = None
	title = None


class NewsfeedListFull(BaseModel):
	"""VK Object NewsfeedListFull

	no_reposts - Information whether reposts hiding is enabled
	source_ids - 
	"""
	no_reposts = None
	source_ids = None
None

class NewsfeedNewsfeedItemType(enum.Enum):
	"""VK Object NewsfeedNewsfeedItemType

	"""
	POST = "post"
	PHOTO = "photo"
	PHOTO_TAG = "photo_tag"
	WALL_PHOTO = "wall_photo"
	FRIEND = "friend"
	AUDIO = "audio"
	VIDEO = "video"
	TOPIC = "topic"
	DIGEST = "digest"
	STORIES = "stories"


class NewsfeedNewsfeedPhoto(BaseModel):
	"""VK Object NewsfeedNewsfeedPhoto

	likes - 
	comments - 
	can_repost - Information whether current user can repost the photo
	"""
	likes = None
	comments = None
	can_repost = None


class NotesNote(BaseModel):
	"""VK Object NotesNote

	read_comments - 
	can_comment - Information whether current user can comment the note
	comments - Comments number
	date - Date when the note has been created in Unixtime
	id - Note ID
	owner_id - Note owner's ID
	text - Note text
	text_wiki - Note text in wiki format
	title - Note title
	view_url - URL of the page with note preview
	"""
	read_comments = None
	can_comment = None
	comments = None
	date = None
	id = None
	owner_id = None
	text = None
	text_wiki = None
	title = None
	view_url = None


class NotesNoteCommeNt(BaseModel):
	"""VK Object NotesNoteCommeNt

	date - Date when the comment has beed added in Unixtime
	id - Comment ID
	message - Comment text
	nid - Note ID
	oid - Note ID
	reply_to - ID of replied comment 
	uid - Comment author's ID
	"""
	date = None
	id = None
	message = None
	nid = None
	oid = None
	reply_to = None
	uid = None


class NotificatioNsFeedback(BaseModel):
	"""VK Object NotificatioNsFeedback

	attachments - 
	from_id - Reply author's ID
	geo - 
	id - Item ID
	likes - 
	text - Reply text
	to_id - Wall owner's ID
	"""
	attachments = None
	from_id = None
	geo = None
	id = None
	likes = None
	text = None
	to_id = None


class NotificatioNsNotificatioN(BaseModel):
	"""VK Object NotificatioNsNotificatioN

	date - Date when the event has been occurred
	feedback - 
	parent - 
	reply - 
	type - Notification type
	"""
	date = None
	feedback = None
	parent = None
	reply = None
	type = None


class NotificatioNsNotificatioNItem(BaseModel):
	"""VK Object NotificatioNsNotificatioNItem

	"""


class NotificatioNsNotificatioNPareNt(BaseModel):
	"""VK Object NotificatioNsNotificatioNPareNt

	"""


class NotificatioNsNotificatioNsCommeNt(BaseModel):
	"""VK Object NotificatioNsNotificatioNsCommeNt

	date - Date when the comment has been added in Unixtime
	id - Comment ID
	owner_id - Author ID
	photo - 
	post - 
	text - Comment text
	topic - 
	video - 
	"""
	date = None
	id = None
	owner_id = None
	photo = None
	post = None
	text = None
	topic = None
	video = None


class NotificatioNsReply(BaseModel):
	"""VK Object NotificatioNsReply

	date - Date when the reply has been created in Unixtime
	id - Reply ID
	text - Reply text
	"""
	date = None
	id = None
	text = None


class NotificatioNsSeNdMessageError(BaseModel):
	"""VK Object NotificatioNsSeNdMessageError

	code - Error code
	description - Error description
	"""
	code = None
	description = None


class NotificatioNsSeNdMessageItem(BaseModel):
	"""VK Object NotificatioNsSeNdMessageItem

	user_id - User ID
	status - Notification status
	error - 
	"""
	user_id = None
	status = None
	error = None


class OauthErrOr(BaseModel):
	"""VK Object OauthErrOr

	error - Error type
	error_description - Error description
	redirect_uri - URI for validation
	"""
	error = None
	error_description = None
	redirect_uri = None


class OrdersAmOunt(BaseModel):
	"""VK Object OrdersAmOunt

	amounts - 
	currency - Currency name
	"""
	amounts = None
	currency = None


class OrdersAmOuntItem(BaseModel):
	"""VK Object OrdersAmOuntItem

	amount - Votes amount in user's currency
	description - Amount description
	votes - Votes number
	"""
	amount = None
	description = None
	votes = None


class OrdersOrder(BaseModel):
	"""VK Object OrdersOrder

	amount - Amount
	app_order_id - App order ID
	cancel_transaction_id - Cancel transaction ID
	date - Date of creation in Unixtime
	id - Order ID
	item - Order item
	receiver_id - Receiver ID
	status - Order status
	transaction_id - Transaction ID
	user_id - User ID
	"""
	amount = None
	app_order_id = None
	cancel_transaction_id = None
	date = None
	id = None
	item = None
	receiver_id = None
	status = None
	transaction_id = None
	user_id = None


class OrdersSubscriptiOn(BaseModel):
	"""VK Object OrdersSubscriptiOn

	cancel_reason - Cancel reason
	create_time - Date of creation in Unixtime
	id - Subscription ID
	item_id - Subscription order item
	next_bill_time - Date of next bill in Unixtime
	pending_cancel - Pending cancel state
	period - Subscription period
	period_start_time - Date of last period start in Unixtime
	price - Subscription price
	status - Subscription status
	test_mode - Is test subscription
	trial_expire_time - Date of trial expire in Unixtime
	update_time - Date of last change in Unixtime
	"""
	cancel_reason = None
	create_time = None
	id = None
	item_id = None
	next_bill_time = None
	pending_cancel = None
	period = None
	period_start_time = None
	price = None
	status = None
	test_mode = None
	trial_expire_time = None
	update_time = None


class OwnerState(BaseModel):
	"""VK Object OwnerState

	state - 
	description - wiki text to describe user state
	"""
	state = None
	description = None


class PagesPrivacySettings(enum.IntEnum):
	"""VK Object PagesPrivacySettings

	"""
	community managers only = 0
	community members only = 1
	everyone = 2


class PagesWikiPage(BaseModel):
	"""VK Object PagesWikiPage

	creator_id - Page creator ID
	creator_name - Page creator name
	editor_id - Last editor ID
	editor_name - Last editor name
	group_id - Community ID
	id - Page ID
	title - Page title
	views - Views number
	who_can_edit - Edit settings of the page
	who_can_view - View settings of the page
	"""
	creator_id = None
	creator_name = None
	editor_id = None
	editor_name = None
	group_id = None
	id = None
	title = None
	views = None
	who_can_edit = None
	who_can_view = None


class PagesWikiPageFull(BaseModel):
	"""VK Object PagesWikiPageFull

	created - Date when the page has been created in Unixtime
	creator_id - Page creator ID
	current_user_can_edit - Information whether current user can edit the page
	current_user_can_edit_access - Information whether current user can edit the page access settings
	edited - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	group_id - Community ID
	html - Page content, HTML
	id - Page ID
	source - Page content, wiki
	title - Page title
	view_url - URL of the page preview
	views - Views number
	who_can_edit - Edit settings of the page
	who_can_view - View settings of the page
	"""
	created = None
	creator_id = None
	current_user_can_edit = None
	current_user_can_edit_access = None
	edited = None
	editor_id = None
	group_id = None
	html = None
	id = None
	source = None
	title = None
	view_url = None
	views = None
	who_can_edit = None
	who_can_view = None


class PagesWikiPageHistory(BaseModel):
	"""VK Object PagesWikiPageHistory

	id - Version ID
	length - Page size in bytes
	date - Date when the page has been edited in Unixtime
	editor_id - Last editor ID
	editor_name - Last editor name
	"""
	id = None
	length = None
	date = None
	editor_id = None
	editor_name = None


class PhotosCommentXtrPid(BaseModel):
	"""VK Object PhotosCommentXtrPid

	attachments - 
	date - Date when the comment has been added in Unixtime
	from_id - Author ID
	id - Comment ID
	likes - 
	pid - Photo ID
	reply_to_comment - Replied comment ID
	reply_to_user - Replied user ID
	text - Comment text
	parents_stack - 
	thread - 
	"""
	attachments = None
	date = None
	from_id = None
	id = None
	likes = None
	pid = None
	reply_to_comment = None
	reply_to_user = None
	text = None
	parents_stack = None
	thread = None


class PhotosImage(BaseModel):
	"""VK Object PhotosImage

	height - Height of the photo in px.
	type - 
	url - Photo URL.
	width - Width of the photo in px.
	"""
	height = None
	type = None
	url = None
	width = None


class PhotosImageTyPe(enum.Enum):
	"""VK Object PhotosImageTyPe

	"""
	S = "s"
	M = "m"
	X = "x"
	L = "l"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	Y = "y"
	Z = "z"
	W = "w"


class PhotosPhoto(BaseModel):
	"""VK Object PhotosPhoto

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	images - 
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_256 - URL of image with 2560 px width
	can_comment - Information whether current user can comment the photo
	place - 
	post_id - Post ID
	sizes - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	has_tags - Whether photo has attached tag links
	restrictions - 
	"""
	access_key = None
	album_id = None
	date = None
	height = None
	id = None
	images = None
	lat = None
	long = None
	owner_id = None
	photo_256 = None
	can_comment = None
	place = None
	post_id = None
	sizes = None
	text = None
	user_id = None
	width = None
	has_tags = None
	restrictions = None


class PhotosPhotoAlbum(BaseModel):
	"""VK Object PhotosPhotoAlbum

	created - Date when the album has been created in Unixtime
	description - Photo album description
	id - Photo album ID
	owner_id - Album owner's ID
	size - Photos number
	thumb - 
	title - Photo album title
	updated - Date when the album has been updated last time in Unixtime
	"""
	created = None
	description = None
	id = None
	owner_id = None
	size = None
	thumb = None
	title = None
	updated = None


class PhotosPhotoAlbumFull(BaseModel):
	"""VK Object PhotosPhotoAlbumFull

	can_upload - Information whether current user can upload photo to the album
	comments_disabled - Information whether album comments are disabled
	created - Date when the album has been created in Unixtime
	description - Photo album description
	id - Photo album ID
	owner_id - Album owner's ID
	size - Photos number
	sizes - 
	thumb_id - Thumb photo ID
	thumb_is_last - Information whether the album thumb is last photo
	thumb_src - URL of the thumb image
	title - Photo album title
	updated - Date when the album has been updated last time in Unixtime
	upload_by_admins_only - Information whether only community administrators can upload photos
	"""
	can_upload = None
	comments_disabled = None
	created = None
	description = None
	id = None
	owner_id = None
	size = None
	sizes = None
	thumb_id = None
	thumb_is_last = None
	thumb_src = None
	title = None
	updated = None
	upload_by_admins_only = None
None

class PhotosPhotoFull(BaseModel):
	"""VK Object PhotosPhotoFull

	access_key - Access key for the photo
	album_id - Album ID
	can_comment - Information whether current user can comment the photo
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	images - 
	lat - Latitude
	likes - 
	reposts - 
	comments - 
	long - Longitude
	owner_id - Photo owner's ID
	post_id - Post ID
	tags - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	can_comment = None
	date = None
	height = None
	id = None
	images = None
	lat = None
	likes = None
	reposts = None
	comments = None
	long = None
	owner_id = None
	post_id = None
	tags = None
	text = None
	user_id = None
	width = None


class PhotosPhotoFullXtrRealOffset(BaseModel):
	"""VK Object PhotosPhotoFullXtrRealOffset

	access_key - Access key for the photo
	album_id - Album ID
	can_comment - 
	comments - 
	date - Date when uploaded
	height - Original photo height
	hidden - Returns if the photo is hidden above the wall
	id - Photo ID
	lat - Latitude
	likes - 
	long - Longitude
	owner_id - Photo owner's ID
	photo_1280 - URL of image with 1280 px width
	photo_130 - URL of image with 130 px width
	photo_2560 - URL of image with 2560 px width
	photo_604 - URL of image with 604 px width
	photo_75 - URL of image with 75 px width
	photo_807 - URL of image with 807 px width
	post_id - Post ID
	real_offset - Real position of the photo
	reposts - 
	sizes - 
	tags - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	can_comment = None
	comments = None
	date = None
	height = None
	hidden = None
	id = None
	lat = None
	likes = None
	long = None
	owner_id = None
	photo_1280 = None
	photo_130 = None
	photo_2560 = None
	photo_604 = None
	photo_75 = None
	photo_807 = None
	post_id = None
	real_offset = None
	reposts = None
	sizes = None
	tags = None
	text = None
	user_id = None
	width = None


class PhotosPhotoSizes(BaseModel):
	"""VK Object PhotosPhotoSizes

	height - Height in px
	url - URL of the image
	src - URL of the image
	type - 
	width - Width in px
	"""
	height = None
	url = None
	src = None
	type = None
	width = None


class PhotosPhotoSizesTyPe(enum.Enum):
	"""VK Object PhotosPhotoSizesTyPe

	"""
	S = "s"
	M = "m"
	X = "x"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	K = "k"
	L = "l"
	Y = "y"
	Z = "z"
	C = "c"
	W = "w"
	A = "a"
	B = "b"
	E = "e"
	I = "i"
	D = "d"
	J = "j"
	TEMP = "temp"
	H = "h"
	G = "g"
	N = "n"
	F = "f"
	MAX = "max"


class PhotosPhotoTag(BaseModel):
	"""VK Object PhotosPhotoTag

	date - Date when tag has been added in Unixtime
	id - Tag ID
	placer_id - ID of the tag creator
	tagged_name - Tag description
	description - Tagged description.
	user_id - Tagged user ID
	viewed - Information whether the tag is reviewed
	x - Coordinate X of the left upper corner
	x2 - Coordinate X of the right lower corner
	y - Coordinate Y of the left upper corner
	y2 - Coordinate Y of the right lower corner
	"""
	date = None
	id = None
	placer_id = None
	tagged_name = None
	description = None
	user_id = None
	viewed = None
	x = None
	x2 = None
	y = None
	y2 = None


class PhotosPhotoUPload(BaseModel):
	"""VK Object PhotosPhotoUPload

	album_id - Album ID
	upload_url - URL to upload photo
	fallback_upload_url - Fallback URL if upload_url returned error
	user_id - User ID
	group_id - Group ID
	"""
	album_id = None
	upload_url = None
	fallback_upload_url = None
	user_id = None
	group_id = None


class PhotosPhotoXtrRealOffset(BaseModel):
	"""VK Object PhotosPhotoXtrRealOffset

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	hidden - Returns if the photo is hidden above the wall
	id - Photo ID
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_1280 - URL of image with 1280 px width
	photo_130 - URL of image with 130 px width
	photo_2560 - URL of image with 2560 px width
	photo_604 - URL of image with 604 px width
	photo_75 - URL of image with 75 px width
	photo_807 - URL of image with 807 px width
	post_id - Post ID
	real_offset - Real position of the photo
	sizes - 
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	date = None
	height = None
	hidden = None
	id = None
	lat = None
	long = None
	owner_id = None
	photo_1280 = None
	photo_130 = None
	photo_2560 = None
	photo_604 = None
	photo_75 = None
	photo_807 = None
	post_id = None
	real_offset = None
	sizes = None
	text = None
	user_id = None
	width = None


class PhotosPhotoXtrTagInfo(BaseModel):
	"""VK Object PhotosPhotoXtrTagInfo

	access_key - Access key for the photo
	album_id - Album ID
	date - Date when uploaded
	height - Original photo height
	id - Photo ID
	lat - Latitude
	long - Longitude
	owner_id - Photo owner's ID
	photo_1280 - URL of image with 1280 px width
	photo_130 - URL of image with 130 px width
	photo_2560 - URL of image with 2560 px width
	photo_604 - URL of image with 604 px width
	photo_75 - URL of image with 75 px width
	photo_807 - URL of image with 807 px width
	placer_id - ID of the tag creator
	post_id - Post ID
	sizes - 
	tag_created - Date when tag has been added in Unixtime
	tag_id - Tag ID
	text - Photo caption
	user_id - ID of the user who have uploaded the photo
	width - Original photo width
	"""
	access_key = None
	album_id = None
	date = None
	height = None
	id = None
	lat = None
	long = None
	owner_id = None
	photo_1280 = None
	photo_130 = None
	photo_2560 = None
	photo_604 = None
	photo_75 = None
	photo_807 = None
	placer_id = None
	post_id = None
	sizes = None
	tag_created = None
	tag_id = None
	text = None
	user_id = None
	width = None


class PhotosTagsSuggestionItem(BaseModel):
	"""VK Object PhotosTagsSuggestionItem

	"""
	title = None
	caption = None
	type = None
	buttons = None
	photo = None
	tags = None
	track_code = None


class PhotosTagsSuggestionItemButton(BaseModel):
	"""VK Object PhotosTagsSuggestionItemButton

	"""
	title = None
	action = None
	style = None


class PodcastCover(BaseModel):
	"""VK Object PodcastCover

	"""
	sizes = None


class PodcastExternalData(BaseModel):
	"""VK Object PodcastExternalData

	url - Url of the podcast page
	owner_url - Url of the podcasts owner community
	title - Podcast title
	owner_name - Name of the podcasts owner community
	cover - Podcast cover
	"""
	url = None
	owner_url = None
	title = None
	owner_name = None
	cover = None


class PollsAnswer(BaseModel):
	"""VK Object PollsAnswer

	id - Answer ID
	rate - Answer rate in percents
	text - Answer text
	votes - Votes number
	"""
	id = None
	rate = None
	text = None
	votes = None


class PollsBackground(BaseModel):
	"""VK Object PollsBackground

	angle - Gradient angle with 0 on positive X axis
	color - Hex color code without #
	height - Original height of pattern tile
	id - 
	name - 
	images - Pattern tiles
	points - Gradient points
	type - 
	width - Original with of pattern tile
	"""
	angle = None
	color = None
	height = None
	id = None
	name = None
	images = None
	points = None
	type = None
	width = None


class PollsFriend(BaseModel):
	"""VK Object PollsFriend

	"""
	id = None


class PollsPoll(BaseModel):
	"""VK Object PollsPoll

	anonymous - 
	friends - 
	multiple - Information whether the poll with multiple choices
	answer_id - Current user's answer ID
	end_date - 
	answer_ids - Current user's answer IDs
	closed - 
	is_board - 
	can_edit - 
	can_vote - 
	can_report - 
	can_share - 
	photo - 
	answers - 
	created - Date when poll has been created in Unixtime
	id - Poll ID
	owner_id - Poll owner's ID
	author_id - Poll author's ID
	question - Poll question
	background - 
	votes - Votes number
	disable_unvote - 
	"""
	anonymous = None
	friends = None
	multiple = None
	answer_id = None
	end_date = None
	answer_ids = None
	closed = None
	is_board = None
	can_edit = None
	can_vote = None
	can_report = None
	can_share = None
	photo = None
	answers = None
	created = None
	id = None
	owner_id = None
	author_id = None
	question = None
	background = None
	votes = None
	disable_unvote = None
None

class PollsVoters(BaseModel):
	"""VK Object PollsVoters

	answer_id - Answer ID
	users - 
	"""
	answer_id = None
	users = None


class PollsVotersUsers(BaseModel):
	"""VK Object PollsVotersUsers

	count - Votes number
	items - 
	"""
	count = None
	items = None


class PrettyCardsPrettyCard(BaseModel):
	"""VK Object PrettyCardsPrettyCard

	button - Button key
	button_text - Button text in current language
	card_id - Card ID (long int returned as string)
	images - 
	link_url - Link URL
	photo - Photo ID (format "<owner_id>_<media_id>")
	price - Price if set (decimal number returned as string)
	price_old - Old price if set (decimal number returned as string)
	title - Title
	"""
	button = None
	button_text = None
	card_id = None
	images = None
	link_url = None
	photo = None
	price = None
	price_old = None
	title = None


class SearchHint(BaseModel):
	"""VK Object SearchHint

	app - 
	description - Object description
	global - Information whether the object has been found globally
	group - 
	profile - 
	section - 
	type - 
	"""
	app = None
	description = None
	_global = None
	group = None
	profile = None
	section = None
	type = None


class SearchHintSection(enum.Enum):
	"""VK Object SearchHintSection

	"""
	GROUPS = "groups"
	EVENTS = "events"
	PUBLICS = "publics"
	CORRESPONDENTS = "correspondents"
	PEOPLE = "people"
	FRIENDS = "friends"
	MUTUAL_FRIENDS = "mutual_friends"


class SearchHintType(enum.Enum):
	"""VK Object SearchHintType

	"""
	GROUP = "group"
	PROFILE = "profile"
	VK_APP = "vk_app"
	APP = "app"
	HTML5_GAME = "html5_game"


class SecureLevel(BaseModel):
	"""VK Object SecureLevel

	level - Level
	uid - User ID
	"""
	level = None
	uid = None


class SecureSmSNotification(BaseModel):
	"""VK Object SecureSmSNotification

	app_id - Application ID
	date - Date when message has been sent in Unixtime
	id - Notification ID
	message - Messsage text
	user_id - User ID
	"""
	app_id = None
	date = None
	id = None
	message = None
	user_id = None


class SecureTokenChecked(BaseModel):
	"""VK Object SecureTokenChecked

	date - Date when access_token has been generated in Unixtime
	expire - Date when access_token will expire in Unixtime
	success - Returns if successfully processed
	user_id - User ID
	"""
	date = None
	expire = None
	success = None
	user_id = None


class SecureTranSaction(BaseModel):
	"""VK Object SecureTranSaction

	date - Transaction date in Unixtime
	id - Transaction ID
	uid_from - From ID
	uid_to - To ID
	votes - Votes number
	"""
	date = None
	id = None
	uid_from = None
	uid_to = None
	votes = None


class StatSActivity(BaseModel):
	"""VK Object StatSActivity

	comments - Comments number
	copies - Reposts number
	hidden - Hidden from news count
	likes - Likes number
	subscribed - New subscribers count
	unsubscribed - Unsubscribed count
	"""
	comments = None
	copies = None
	hidden = None
	likes = None
	subscribed = None
	unsubscribed = None


class StatSCity(BaseModel):
	"""VK Object StatSCity

	count - Visitors number
	name - City name
	value - City ID
	"""
	count = None
	name = None
	value = None


class StatSCountry(BaseModel):
	"""VK Object StatSCountry

	code - Country code
	count - Visitors number
	name - Country name
	value - Country ID
	"""
	code = None
	count = None
	name = None
	value = None


class StatSPeriod(BaseModel):
	"""VK Object StatSPeriod

	activity - 
	period_from - Unix timestamp
	period_to - Unix timestamp
	reach - 
	visitors - 
	"""
	activity = None
	period_from = None
	period_to = None
	reach = None
	visitors = None


class StatSReach(BaseModel):
	"""VK Object StatSReach

	age - 
	cities - 
	countries - 
	mobile_reach - Reach count from mobile devices
	reach - Reach count
	reach_subscribers - Subscribers reach count
	sex - 
	sex_age - 
	"""
	age = None
	cities = None
	countries = None
	mobile_reach = None
	reach = None
	reach_subscribers = None
	sex = None
	sex_age = None


class StatSSexAge(BaseModel):
	"""VK Object StatSSexAge

	count - Visitors number
	value - Sex/age value
	reach - 
	reach_subscribers - 
	count_subscribers - 
	"""
	count = None
	value = None
	reach = None
	reach_subscribers = None
	count_subscribers = None


class StatSViewS(BaseModel):
	"""VK Object StatSViewS

	age - 
	cities - 
	countries - 
	mobile_views - Number of views from mobile devices
	sex - 
	sex_age - 
	views - Views number
	visitors - Visitors number
	"""
	age = None
	cities = None
	countries = None
	mobile_views = None
	sex = None
	sex_age = None
	views = None
	visitors = None


class StatSWallpoStStat(BaseModel):
	"""VK Object StatSWallpoStStat

	post_id - 
	hide - Hidings number
	join_group - People have joined the group
	links - Link clickthrough
	reach_subscribers - Subscribers reach
	reach_subscribers_count - 
	reach_total - Total reach
	reach_total_count - 
	reach_viral - 
	reach_ads - 
	report - Reports number
	to_group - Clickthrough to community
	unsubscribe - Unsubscribed members
	sex_age - 
	"""
	post_id = None
	hide = None
	join_group = None
	links = None
	reach_subscribers = None
	reach_subscribers_count = None
	reach_total = None
	reach_total_count = None
	reach_viral = None
	reach_ads = None
	report = None
	to_group = None
	unsubscribe = None
	sex_age = None


class StatuSStatuS(BaseModel):
	"""VK Object StatuSStatuS

	text - Status text
	audio - 
	"""
	text = None
	audio = None


class StickerSImageSet(BaseModel):
	"""VK Object StickerSImageSet

	base_url - Base URL for images in set
	version - Version number to be appended to the image URL
	"""
	base_url = None
	version = None


class StorageValue(BaseModel):
	"""VK Object StorageValue

	"""
	key = None
	value = None


class StoreProduct(BaseModel):
	"""VK Object StoreProduct

	id - Id of the product
	type - Product type
	purchased - Information whether the product is purchased (1 - yes, 0 - no)
	active - Information whether the product is active (1 - yes, 0 - no)
	promoted - Information whether the product is promoted (1 - yes, 0 - no)
	purchase_date - Date (Unix time) when the product was purchased
	title - Title of the product
	stickers - 
	icon - Array of icon images or icon set object of the product (for stickers product type)
	previews - Array of preview images of the product (for stickers product type)
	has_animation - Information whether the product is an animated sticker pack (for stickers product type)
	subtitle - Subtitle of the product
	"""
	id = None
	type = None
	purchased = None
	active = None
	promoted = None
	purchase_date = None
	title = None
	stickers = None
	icon = None
	previews = None
	has_animation = None
	subtitle = None
None

class StoreStickerSKeyword(BaseModel):
	"""VK Object StoreStickerSKeyword

	"""
	words = None
	user_stickers = None
	promoted_stickers = None
	stickers = None


class StoreStickerSKeywordSticker(BaseModel):
	"""VK Object StoreStickerSKeywordSticker

	pack_id - Pack id
	sticker_id - Sticker id
	"""
	pack_id = None
	sticker_id = None


class StoreStickerSKeywordStickerS(BaseModel):
	"""VK Object StoreStickerSKeywordStickerS

	"""


class StorieSClickableArea(BaseModel):
	"""VK Object StorieSClickableArea

	"""
	x = None
	y = None


class StorieSClickableSticker(BaseModel):
	"""VK Object StorieSClickableSticker

	clickable_area - 
	id - Clickable sticker ID
	hashtag - 
	link_object - 
	mention - 
	tooltip_text - 
	owner_id - 
	story_id - 
	question - 
	question_button - 
	place_id - 
	market_item - 
	audio - 
	audio_start_time - 
	style - 
	type - 
	subtype - 
	post_owner_id - 
	post_id - 
	poll - 
	color - Color, hex format
	sticker_id - Sticker ID
	sticker_pack_id - Sticker pack ID
	app - 
	app_context - Additional context for app sticker
	has_new_interactions - Whether current user has unread interaction with this app
	is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
	situational_theme_id - 
	situational_app_url - 
	"""
	clickable_area = None
	id = None
	hashtag = None
	link_object = None
	mention = None
	tooltip_text = None
	owner_id = None
	story_id = None
	question = None
	question_button = None
	place_id = None
	market_item = None
	audio = None
	audio_start_time = None
	style = None
	type = None
	subtype = None
	post_owner_id = None
	post_id = None
	poll = None
	color = None
	sticker_id = None
	sticker_pack_id = None
	app = None
	app_context = None
	has_new_interactions = None
	is_broadcast_notify_allowed = None
	situational_theme_id = None
	situational_app_url = None


class StorieSClickableStickerS(BaseModel):
	"""VK Object StorieSClickableStickerS

	"""
	clickable_stickers = None
	original_height = None
	original_width = None


class StorieSFeedItem(BaseModel):
	"""VK Object StorieSFeedItem

	type - Type of Feed Item
	id - 
	stories - Author stories
	grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
	app - App, which stories has been grouped (for type app_grouped_stories)
	promo_data - Additional data for promo stories (for type promo_stories)
	birthday_user_id - 
	"""
	type = None
	id = None
	stories = None
	grouped = None
	app = None
	promo_data = None
	birthday_user_id = None


class StorieSPromoBlock(BaseModel):
	"""VK Object StorieSPromoBlock

	name - Promo story title
	photo_50 - RL of square photo of the story with 50 pixels in width
	photo_100 - RL of square photo of the story with 100 pixels in width
	not_animated - Hide animation for promo story
	"""
	name = None
	photo_50 = None
	photo_100 = None
	not_animated = None


class StorieSReplieS(BaseModel):
	"""VK Object StorieSReplieS

	count - Replies number.
	new - New replies number.
	"""
	count = None
	new = None


class StorieSStatLine(BaseModel):
	"""VK Object StorieSStatLine

	"""
	name = None
	counter = None
	is_unavailable = None


class StorieSStory(BaseModel):
	"""VK Object StorieSStory

	access_key - Access key for private object.
	can_comment - Information whether current user can comment the story (0 - no, 1 - yes).
	can_reply - Information whether current user can reply to the story (0 - no, 1 - yes).
	can_see - Information whether current user can see the story (0 - no, 1 - yes).
	can_like - Information whether current user can like the story.
	can_share - Information whether current user can share the story (0 - no, 1 - yes).
	can_hide - Information whether current user can hide the story (0 - no, 1 - yes).
	date - Date when story has been added in Unixtime.
	expires_at - Story expiration time. Unixtime.
	id - Story ID.
	is_deleted - Information whether the story is deleted (false - no, true - yes).
	is_expired - Information whether the story is expired (false - no, true - yes).
	link - 
	owner_id - Story owner's ID.
	parent_story - 
	parent_story_access_key - Access key for private object.
	parent_story_id - Parent story ID.
	parent_story_owner_id - Parent story owner's ID.
	photo - 
	replies - Replies counters to current story.
	seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
	type - 
	clickable_stickers - 
	video - 
	views - Views number.
	can_ask - Information whether story has question sticker and current user can send question to the author
	can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
	narratives_count - 
	first_narrative_title - 
	birthday_wish_user_id - 
	can_use_in_narrative - 
	"""
	access_key = None
	can_comment = None
	can_reply = None
	can_see = None
	can_like = None
	can_share = None
	can_hide = None
	date = None
	expires_at = None
	id = None
	is_deleted = None
	is_expired = None
	link = None
	owner_id = None
	parent_story = None
	parent_story_access_key = None
	parent_story_id = None
	parent_story_owner_id = None
	photo = None
	replies = None
	seen = None
	type = None
	clickable_stickers = None
	video = None
	views = None
	can_ask = None
	can_ask_anonymous = None
	narratives_count = None
	first_narrative_title = None
	birthday_wish_user_id = None
	can_use_in_narrative = None


class StorieSStoryLink(BaseModel):
	"""VK Object StorieSStoryLink

	text - Link text
	url - Link URL
	"""
	text = None
	url = None


class StorieSStoryStatS(BaseModel):
	"""VK Object StorieSStoryStatS

	"""
	answer = None
	bans = None
	open_link = None
	replies = None
	shares = None
	subscribers = None
	views = None
	likes = None


class StorieSStoryStatSStat(BaseModel):
	"""VK Object StorieSStoryStatSStat

	count - Stat value
	state - 
	"""
	count = None
	state = None


class StorieSStoryStatSState(enum.Enum):
	"""VK Object StorieSStoryStatSState

	"""
	ON = "on"
	OFF = "off"
	HIDDEN = "hidden"


class StorieSStoryType(enum.Enum):
	"""VK Object StorieSStoryType

	"""
	PHOTO = "photo"
	VIDEO = "video"
	LIVE_ACTIVE = "live_active"
	LIVE_FINISHED = "live_finished"
	BIRTHDAY_INVITE = "birthday_invite"


class StorieSUploadLinkText(enum.Enum):
	"""VK Object StorieSUploadLinkText

	"""
	TO_STORE = "to_store"
	VOTE = "vote"
	MORE = "more"
	BOOK = "book"
	ORDER = "order"
	ENROLL = "enroll"
	FILL = "fill"
	SIGNUP = "signup"
	BUY = "buy"
	TICKET = "ticket"
	WRITE = "write"
	OPEN = "open"
	LEARN_MORE = "learn_more"
	VIEW = "view"
	GO_TO = "go_to"
	CONTACT = "contact"
	WATCH = "watch"
	PLAY = "play"
	INSTALL = "install"
	READ = "read"
	CALENDAR = "calendar"


class StorieSViewerSItem(BaseModel):
	"""VK Object StorieSViewerSItem

	is_liked - user has like for this object
	user_id - user id
	user - 
	"""
	is_liked = None
	user_id = None
	user = None


class UsersCareer(BaseModel):
	"""VK Object UsersCareer

	city_id - City ID
	city_name - City name
	company - Company name
	country_id - Country ID
	from - From year
	group_id - Community ID
	id - Career ID
	position - Position
	until - Till year
	"""
	city_id = None
	city_name = None
	company = None
	country_id = None
	_from = None
	group_id = None
	id = None
	position = None
	until = None


class UsersExports(BaseModel):
	"""VK Object UsersExports

	"""
	facebook = None
	livejournal = None
	twitter = None


class UsersFields(enum.Enum):
	"""VK Object UsersFields

	"""
	FIRST_NAME_NOM = "first_name_nom"
	FIRST_NAME_GEN = "first_name_gen"
	FIRST_NAME_DAT = "first_name_dat"
	FIRST_NAME_ACC = "first_name_acc"
	FIRST_NAME_INS = "first_name_ins"
	FIRST_NAME_ABL = "first_name_abl"
	LAST_NAME_NOM = "last_name_nom"
	LAST_NAME_GEN = "last_name_gen"
	LAST_NAME_DAT = "last_name_dat"
	LAST_NAME_ACC = "last_name_acc"
	LAST_NAME_INS = "last_name_ins"
	LAST_NAME_ABL = "last_name_abl"
	PHOTO_ID = "photo_id"
	VERIFIED = "verified"
	SEX = "sex"
	BDATE = "bdate"
	CITY = "city"
	COUNTRY = "country"
	HOME_TOWN = "home_town"
	HAS_PHOTO = "has_photo"
	PHOTO_50 = "photo_50"
	PHOTO_100 = "photo_100"
	PHOTO_200_ORIG = "photo_200_orig"
	PHOTO_200 = "photo_200"
	PHOTO_400 = "photo_400"
	PHOTO_400_ORIG = "photo_400_orig"
	PHOTO_MAX = "photo_max"
	PHOTO_MAX_ORIG = "photo_max_orig"
	PHOTO_MAX_SIZE = "photo_max_size"
	ONLINE = "online"
	LISTS = "lists"
	DOMAIN = "domain"
	HAS_MOBILE = "has_mobile"
	CONTACTS = "contacts"
	SITE = "site"
	EDUCATION = "education"
	UNIVERSITIES = "universities"
	SCHOOLS = "schools"
	STATUS = "status"
	LAST_SEEN = "last_seen"
	FOLLOWERS_COUNT = "followers_count"
	COUNTERS = "counters"
	COMMON_COUNT = "common_count"
	OCCUPATION = "occupation"
	NICKNAME = "nickname"
	RELATIVES = "relatives"
	RELATION = "relation"
	PERSONAL = "personal"
	CONNECTIONS = "connections"
	EXPORTS = "exports"
	WALL_COMMENTS = "wall_comments"
	ACTIVITIES = "activities"
	INTERESTS = "interests"
	MUSIC = "music"
	MOVIES = "movies"
	TV = "tv"
	BOOKS = "books"
	GAMES = "games"
	ABOUT = "about"
	QUOTES = "quotes"
	CAN_POST = "can_post"
	CAN_SEE_ALL_POSTS = "can_see_all_posts"
	CAN_SEE_AUDIO = "can_see_audio"
	CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
	CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
	IS_FAVORITE = "is_favorite"
	IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
	TIMEZONE = "timezone"
	SCREEN_NAME = "screen_name"
	MAIDEN_NAME = "maiden_name"
	CROP_PHOTO = "crop_photo"
	IS_FRIEND = "is_friend"
	FRIEND_STATUS = "friend_status"
	CAREER = "career"
	MILITARY = "military"
	BLACKLISTED = "blacklisted"
	BLACKLISTED_BY_ME = "blacklisted_by_me"
	CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
	DESCRIPTIONS = "descriptions"
	TRENDING = "trending"
	MUTUAL = "mutual"
	FRIENDSHIP_WEEKS = "friendship_weeks"
	CAN_INVITE_TO_CHATS = "can_invite_to_chats"
	STORIES_ARCHIVE_COUNT = "stories_archive_count"
	VIDEO_LIVE_LEVEL = "video_live_level"
	VIDEO_LIVE_COUNT = "video_live_count"
	CLIPS_COUNT = "clips_count"
	SERVICE_DESCRIPTION = "service_description"
	IS_DEAD = "is_dead"


class UsersLastSeen(BaseModel):
	"""VK Object UsersLastSeen

	platform - Type of the platform that used for the last authorization
	time - Last visit date (in Unix time)
	"""
	platform = None
	time = None


class UsersMilitary(BaseModel):
	"""VK Object UsersMilitary

	country_id - Country ID
	from - From year
	id - Military ID
	unit - Unit name
	unit_id - Unit ID
	until - Till year
	"""
	country_id = None
	_from = None
	id = None
	unit = None
	unit_id = None
	until = None


class UsersOccUpation(BaseModel):
	"""VK Object UsersOccUpation

	id - ID of school, university, company group
	name - Name of occupation
	type - Type of occupation
	"""
	id = None
	name = None
	type = None


class UsersOnlineInfo(BaseModel):
	"""VK Object UsersOnlineInfo

	visible - Whether you can see real online status of user or not
	last_seen - Last time we saw user being active
	is_online - Whether user is currently online or not
	app_id - Application id from which user is currently online or was last seen online
	is_mobile - Is user online from desktop app or mobile app
	status - In case user online is not visible, it indicates approximate timeframe of user online
	"""
	visible = None
	last_seen = None
	is_online = None
	app_id = None
	is_mobile = None
	status = None


class UsersPersonal(BaseModel):
	"""VK Object UsersPersonal

	alcohol - User's views on alcohol
	inspired_by - User's inspired by
	langs - 
	life_main - User's personal priority in life
	people_main - User's personal priority in people
	political - User's political views
	religion - User's religion
	religion_id - User's religion id
	smoking - User's views on smoking
	"""
	alcohol = None
	inspired_by = None
	langs = None
	life_main = None
	people_main = None
	political = None
	religion = None
	religion_id = None
	smoking = None


class UsersRelative(BaseModel):
	"""VK Object UsersRelative

	birth_date - Date of child birthday (format dd.mm.yyyy)
	id - Relative ID
	name - Name of relative
	type - Relative type
	"""
	birth_date = None
	id = None
	name = None
	type = None


class UsersSchool(BaseModel):
	"""VK Object UsersSchool

	city - City ID
	class - School class letter
	country - Country ID
	id - School ID
	name - School name
	type - School type ID
	type_str - School type name
	year_from - Year the user started to study
	year_graduated - Graduation year
	year_to - Year the user finished to study
	speciality - 
	"""
	city = None
	_class = None
	country = None
	id = None
	name = None
	type = None
	type_str = None
	year_from = None
	year_graduated = None
	year_to = None
	speciality = None
None

class UsersUniversity(BaseModel):
	"""VK Object UsersUniversity

	chair - Chair ID
	chair_name - Chair name
	city - City ID
	country - Country ID
	education_form - Education form
	education_status - Education status
	faculty - Faculty ID
	faculty_name - Faculty name
	graduation - Graduation year
	id - University ID
	name - University name
	university_group_id - 
	"""
	chair = None
	chair_name = None
	city = None
	country = None
	education_form = None
	education_status = None
	faculty = None
	faculty_name = None
	graduation = None
	id = None
	name = None
	university_group_id = None


class UsersUser(BaseModel):
	"""VK Object UsersUser

	sex - User sex
	screen_name - Domain name of the user's page
	photo_50 - URL of square photo of the user with 50 pixels in width
	photo_100 - URL of square photo of the user with 100 pixels in width
	online_info - 
	online - Information whether the user is online
	online_mobile - Information whether the user is online in mobile site or application
	online_app - Application ID
	verified - Information whether the user is verified
	trending - Information whether the user has a "fire" pictogram.
	friend_status - 
	mutual - 
	"""
	sex = None
	screen_name = None
	photo_50 = None
	photo_100 = None
	online_info = None
	online = None
	online_mobile = None
	online_app = None
	verified = None
	trending = None
	friend_status = None
	mutual = None


class UsersUserConnections(BaseModel):
	"""VK Object UsersUserConnections

	skype - User's Skype nickname
	facebook - User's Facebook account
	facebook_name - User's Facebook name
	twitter - User's Twitter account
	livejournal - User's Livejournal account
	instagram - User's Instagram account
	"""
	skype = None
	facebook = None
	facebook_name = None
	twitter = None
	livejournal = None
	instagram = None


class UsersUserCoUnters(BaseModel):
	"""VK Object UsersUserCoUnters

	albums - Albums number
	audios - Audios number
	followers - Followers number
	friends - Friends number
	gifts - Gifts number
	groups - Communities number
	notes - Notes number
	online_friends - Online friends number
	pages - Public pages number
	photos - Photos number
	subscriptions - Subscriptions number
	user_photos - Number of photos with user
	user_videos - Number of videos with user
	videos - Videos number
	new_photo_tags - 
	new_recognition_tags - 
	mutual_friends - 
	posts - 
	articles - 
	wishes - 
	podcasts - 
	clips - 
	clips_followers - 
	"""
	albums = None
	audios = None
	followers = None
	friends = None
	gifts = None
	groups = None
	notes = None
	online_friends = None
	pages = None
	photos = None
	subscriptions = None
	user_photos = None
	user_videos = None
	videos = None
	new_photo_tags = None
	new_recognition_tags = None
	mutual_friends = None
	posts = None
	articles = None
	wishes = None
	podcasts = None
	clips = None
	clips_followers = None


class UsersUserFUll(BaseModel):
	"""VK Object UsersUserFUll

	first_name_nom - User's first name in nominative case
	first_name_gen - User's first name in genitive case
	first_name_dat - User's first name in dative case
	first_name_acc - User's first name in accusative case
	first_name_ins - User's first name in instrumental case
	first_name_abl - User's first name in prepositional case
	last_name_nom - User's last name in nominative case
	last_name_gen - User's last name in genitive case
	last_name_dat - User's last name in dative case
	last_name_acc - User's last name in accusative case
	last_name_ins - User's last name in instrumental case
	last_name_abl - User's last name in prepositional case
	nickname - User nickname
	maiden_name - User maiden name
	contact_name - User contact name
	domain - Domain name of the user's page
	bdate - User's date of birth
	city - 
	country - 
	timezone - User's timezone
	owner_state - 
	photo_200 - URL of square photo of the user with 200 pixels in width
	photo_max - URL of square photo of the user with maximum width
	photo_200_orig - URL of user's photo with 200 pixels in width
	photo_400_orig - URL of user's photo with 400 pixels in width
	photo_max_orig - URL of user's photo of maximum size
	photo_id - ID of the user's main photo
	has_photo - Information whether the user has main photo
	has_mobile - Information whether the user specified his phone number
	is_friend - Information whether the user is a friend of current user
	wall_comments - Information whether current user can comment wall posts
	can_post - Information whether current user can post on the user's wall
	can_see_all_posts - Information whether current user can see other users' audio on the wall
	can_see_audio - Information whether current user can see the user's audio
	type - 
	email - 
	skype - 
	facebook - 
	facebook_name - 
	twitter - 
	livejournal - 
	instagram - 
	test - 
	video_live - 
	is_video_live_notifications_blocked - 
	is_service - 
	service_description - 
	photo_rec - 
	photo_medium - 
	photo_medium_rec - 
	photo - 
	photo_big - 
	photo_400 - 
	photo_max_size - 
	language - 
	stories_archive_count - 
	wall_default - 
	can_call - Information whether current user can call
	can_see_wishes - Information whether current user can see the user's wishes
	can_see_gifts - Information whether current user can see the user's gifts
	interests - 
	books - 
	tv - 
	quotes - 
	about - 
	games - 
	movies - 
	activities - 
	music - 
	can_write_private_message - Information whether current user can write private message
	can_send_friend_request - Information whether current user can send a friend request
	can_be_invited_group - Information whether current user can be invited to the community
	mobile_phone - User's mobile phone number
	home_phone - User's additional phone number
	site - User's website
	status_audio - 
	status - User's status
	activity - User's status
	last_seen - 
	exports - 
	crop_photo - 
	followers_count - Number of user's followers
	video_live_level - User level in live streams achievements
	video_live_count - Number of user's live streams
	clips_count - Number of user's clips
	blacklisted - Information whether current user is in the requested user's blacklist.
	blacklisted_by_me - Information whether the requested user is in current user's blacklist
	is_favorite - Information whether the requested user is in faves of current user
	is_hidden_from_feed - Information whether the requested user is hidden from current user's newsfeed
	common_count - Number of common friends with current user
	occupation - 
	career - 
	military - 
	university - University ID
	university_name - University name
	university_group_id - 
	faculty - Faculty ID
	faculty_name - Faculty name
	graduation - Graduation year
	education_form - Education form
	education_status - User's education status
	home_town - User hometown
	relation - User relationship status
	relation_partner - 
	personal - 
	universities - 
	schools - 
	relatives - 
	is_subscribed_podcasts - Information whether current user is subscribed to podcasts
	can_subscribe_podcasts - Owner in whitelist or not
	can_subscribe_posts - Can subscribe to wall
	counters - 
	access_key - 
	can_upload_doc - 
	hash - 
	has_email - 
	"""
	first_name_nom = None
	first_name_gen = None
	first_name_dat = None
	first_name_acc = None
	first_name_ins = None
	first_name_abl = None
	last_name_nom = None
	last_name_gen = None
	last_name_dat = None
	last_name_acc = None
	last_name_ins = None
	last_name_abl = None
	nickname = None
	maiden_name = None
	contact_name = None
	domain = None
	bdate = None
	city = None
	country = None
	timezone = None
	owner_state = None
	photo_200 = None
	photo_max = None
	photo_200_orig = None
	photo_400_orig = None
	photo_max_orig = None
	photo_id = None
	has_photo = None
	has_mobile = None
	is_friend = None
	wall_comments = None
	can_post = None
	can_see_all_posts = None
	can_see_audio = None
	type = None
	email = None
	skype = None
	facebook = None
	facebook_name = None
	twitter = None
	livejournal = None
	instagram = None
	test = None
	video_live = None
	is_video_live_notifications_blocked = None
	is_service = None
	service_description = None
	photo_rec = None
	photo_medium = None
	photo_medium_rec = None
	photo = None
	photo_big = None
	photo_400 = None
	photo_max_size = None
	language = None
	stories_archive_count = None
	wall_default = None
	can_call = None
	can_see_wishes = None
	can_see_gifts = None
	interests = None
	books = None
	tv = None
	quotes = None
	about = None
	games = None
	movies = None
	activities = None
	music = None
	can_write_private_message = None
	can_send_friend_request = None
	can_be_invited_group = None
	mobile_phone = None
	home_phone = None
	site = None
	status_audio = None
	status = None
	activity = None
	last_seen = None
	exports = None
	crop_photo = None
	followers_count = None
	video_live_level = None
	video_live_count = None
	clips_count = None
	blacklisted = None
	blacklisted_by_me = None
	is_favorite = None
	is_hidden_from_feed = None
	common_count = None
	occupation = None
	career = None
	military = None
	university = None
	university_name = None
	university_group_id = None
	faculty = None
	faculty_name = None
	graduation = None
	education_form = None
	education_status = None
	home_town = None
	relation = None
	relation_partner = None
	personal = None
	universities = None
	schools = None
	relatives = None
	is_subscribed_podcasts = None
	can_subscribe_podcasts = None
	can_subscribe_posts = None
	counters = None
	access_key = None
	can_upload_doc = None
	hash = None
	has_email = None


class UsersUserMin(BaseModel):
	"""VK Object UsersUserMin

	deactivated - Returns if a profile is deleted or blocked
	first_name - User first name
	hidden - Returns if a profile is hidden.
	id - User ID
	last_name - User last name
	can_access_closed - 
	is_closed - 
	"""
	deactivated = None
	first_name = None
	hidden = None
	id = None
	last_name = None
	can_access_closed = None
	is_closed = None


class UsersUserRelation(enum.IntEnum):
	"""VK Object UsersUserRelation

	"""
	not specified = 0
	single = 1
	in a relationship = 2
	engaged = 3
	married = 4
	complicated = 5
	actively searching = 6
	in love = 7
	in a civil union = 8


class UsersUserSettingsXtr(BaseModel):
	"""VK Object UsersUserSettingsXtr

	connections - 
	bdate - User's date of birth
	bdate_visibility - Information whether user's birthdate are hidden
	city - 
	country - 
	first_name - User first name
	home_town - User's hometown
	last_name - User last name
	maiden_name - User maiden name
	name_request - 
	personal - 
	phone - User phone number with some hidden digits
	relation - User relationship status
	relation_partner - 
	relation_pending - Information whether relation status is pending
	relation_requests - 
	screen_name - Domain name of the user's page
	sex - User sex
	status - User status
	status_audio - 
	interests - 
	languages - 
	"""
	connections = None
	bdate = None
	bdate_visibility = None
	city = None
	country = None
	first_name = None
	home_town = None
	last_name = None
	maiden_name = None
	name_request = None
	personal = None
	phone = None
	relation = None
	relation_partner = None
	relation_pending = None
	relation_requests = None
	screen_name = None
	sex = None
	status = None
	status_audio = None
	interests = None
	languages = None


class UsersUserType(enum.Enum):
	"""VK Object UsersUserType

	"""
	PROFILE = "profile"


class UsersUserXtrCoUnters(BaseModel):
	"""VK Object UsersUserXtrCoUnters

	"""


class UsersUserXtrType(BaseModel):
	"""VK Object UsersUserXtrType

	"""
	type = None


class UsersUsersArray(BaseModel):
	"""VK Object UsersUsersArray

	count - Users number
	items - 
	"""
	count = None
	items = None


class UtilsDomainResolved(BaseModel):
	"""VK Object UtilsDomainResolved

	object_id - Object ID
	group_id - Group ID
	type - 
	"""
	object_id = None
	group_id = None
	type = None


class UtilsDomainResolvedType(enum.Enum):
	"""VK Object UtilsDomainResolvedType

	"""
	USER = "user"
	GROUP = "group"
	APPLICATION = "application"
	PAGE = "page"
	VK_APP = "vk_app"
	COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
	"""VK Object UtilsLastShortenedLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	timestamp - Creation time in Unixtime
	url - Full URL
	views - Total views number
	"""
	access_key = None
	key = None
	short_url = None
	timestamp = None
	url = None
	views = None


class UtilsLinkChecked(BaseModel):
	"""VK Object UtilsLinkChecked

	link - Link URL
	status - 
	"""
	link = None
	status = None


class UtilsLinkCheckedStatUs(enum.Enum):
	"""VK Object UtilsLinkCheckedStatUs

	"""
	NOT_BANNED = "not_banned"
	BANNED = "banned"
	PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
	"""VK Object UtilsLinkStats

	key - Link key (characters after vk.cc/)
	stats - 
	"""
	key = None
	stats = None


class UtilsLinkStatsExtended(BaseModel):
	"""VK Object UtilsLinkStatsExtended

	key - Link key (characters after vk.cc/)
	stats - 
	"""
	key = None
	stats = None


class UtilsShortLink(BaseModel):
	"""VK Object UtilsShortLink

	access_key - Access key for private stats
	key - Link key (characters after vk.cc/)
	short_url - Short link URL
	url - Full URL
	"""
	access_key = None
	key = None
	short_url = None
	url = None


class UtilsStats(BaseModel):
	"""VK Object UtilsStats

	timestamp - Start time
	views - Total views number
	"""
	timestamp = None
	views = None


class UtilsStatsCity(BaseModel):
	"""VK Object UtilsStatsCity

	city_id - City ID
	views - Views number
	"""
	city_id = None
	views = None


class UtilsStatsCoUntry(BaseModel):
	"""VK Object UtilsStatsCoUntry

	country_id - Country ID
	views - Views number
	"""
	country_id = None
	views = None


class UtilsStatsExtended(BaseModel):
	"""VK Object UtilsStatsExtended

	cities - 
	countries - 
	sex_age - 
	timestamp - Start time
	views - Total views number
	"""
	cities = None
	countries = None
	sex_age = None
	timestamp = None
	views = None


class UtilsStatsSexAge(BaseModel):
	"""VK Object UtilsStatsSexAge

	age_range - Age denotation
	female -  Views by female users
	male -  Views by male users
	"""
	age_range = None
	female = None
	male = None


class VideoLiVeInfo(BaseModel):
	"""VK Object VideoLiVeInfo

	"""
	enabled = None
	is_notifications_blocked = None


class VideoLiVeSettings(BaseModel):
	"""VK Object VideoLiVeSettings

	can_rewind - If user car rewind live or not
	is_endless - If live is endless or not
	max_duration - Max possible time for rewind
	"""
	can_rewind = None
	is_endless = None
	max_duration = None


class VideoRestrictionButton(BaseModel):
	"""VK Object VideoRestrictionButton

	"""
	action = None
	title = None


class VideoSaVeResult(BaseModel):
	"""VK Object VideoSaVeResult

	access_key - Video access key
	description - Video description
	owner_id - Video owner ID
	title - Video title
	upload_url - URL for the video uploading
	video_id - Video ID
	"""
	access_key = None
	description = None
	owner_id = None
	title = None
	upload_url = None
	video_id = None


class VideoVideo(BaseModel):
	"""VK Object VideoVideo

	access_key - Video access key
	adding_date - Date when the video has been added in Unixtime
	can_comment - Information whether current user can comment the video
	can_edit - Information whether current user can edit the video
	can_like - Information whether current user can like the video
	can_repost - Information whether current user can repost the video
	can_subscribe - Information whether current user can subscribe to author of the video
	can_add_to_faves - Information whether current user can add the video to favourites
	can_add - Information whether current user can add the video
	can_attach_link - Information whether current user can attach action button to the video
	is_private - 1 if video is private
	comments - Number of comments
	date - Date when video has been uploaded in Unixtime
	description - Video description
	duration - Video duration in seconds
	image - 
	first_frame - 
	width - Video width
	height - Video height
	id - Video ID
	owner_id - Video owner ID
	user_id - Id of the user who uploaded the video if it was uploaded to a group by member
	title - Video title
	is_favorite - Whether video is added to bookmarks
	player - Video embed URL
	processing - Returns if the video is processing
	converting - 1 if  video is being converted
	restriction - 
	added - 1 if video is added to user's albums
	is_subscribed - 1 if user is subscribed to author of the video
	track_code - 
	repeat - Information whether the video is repeated
	type - 
	views - Number of views
	local_views - If video is external, number of views on vk
	content_restricted - Restriction code
	content_restricted_message - Restriction text
	balance - Live donations balance
	live_status - Live stream status
	live - 1 if the video is a live stream
	upcoming - 1 if the video is an upcoming stream
	live_start_time - Date in Unixtime when the live stream is scheduled to start by the author
	live_notify - Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)
	spectators - Number of spectators of the stream
	platform - External platform
	likes - 
	reposts - 
	"""
	access_key = None
	adding_date = None
	can_comment = None
	can_edit = None
	can_like = None
	can_repost = None
	can_subscribe = None
	can_add_to_faves = None
	can_add = None
	can_attach_link = None
	is_private = None
	comments = None
	date = None
	description = None
	duration = None
	image = None
	first_frame = None
	width = None
	height = None
	id = None
	owner_id = None
	user_id = None
	title = None
	is_favorite = None
	player = None
	processing = None
	converting = None
	restriction = None
	added = None
	is_subscribed = None
	track_code = None
	repeat = None
	type = None
	views = None
	local_views = None
	content_restricted = None
	content_restricted_message = None
	balance = None
	live_status = None
	live = None
	upcoming = None
	live_start_time = None
	live_notify = None
	spectators = None
	platform = None
	likes = None
	reposts = None


class VideoVideoAlbumFull(BaseModel):
	"""VK Object VideoVideoAlbumFull

	count - Total number of videos in album
	id - Album ID
	image - Album cover image in different sizes
	image_blur - Need blur album thumb or not
	is_system - Information whether album is system
	owner_id - Album owner's ID
	title - Album title
	updated_time - Date when the album has been updated last time in Unixtime
	"""
	count = None
	id = None
	image = None
	image_blur = None
	is_system = None
	owner_id = None
	title = None
	updated_time = None


class VideoVideoFiles(BaseModel):
	"""VK Object VideoVideoFiles

	external - URL of the external player
	mp4_240 - URL of the mpeg4 file with 240p quality
	mp4_360 - URL of the mpeg4 file with 360p quality
	mp4_480 - URL of the mpeg4 file with 480p quality
	mp4_720 - URL of the mpeg4 file with 720p quality
	mp4_1080 - URL of the mpeg4 file with 1080p quality
	flv_320 - URL of the flv file with 320p quality
	"""
	external = None
	mp4_240 = None
	mp4_360 = None
	mp4_480 = None
	mp4_720 = None
	mp4_1080 = None
	flv_320 = None


class VideoVideoFull(BaseModel):
	"""VK Object VideoVideoFull

	files - 
	live_settings - Settings for live stream
	"""
	files = None
	live_settings = None


class VideoVideoImage(BaseModel):
	"""VK Object VideoVideoImage

	"""
	with_padding = None


class WallAppPost(BaseModel):
	"""VK Object WallAppPost

	id - Application ID
	name - Application name
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id = None
	name = None
	photo_130 = None
	photo_604 = None


class WallAttachedNote(BaseModel):
	"""VK Object WallAttachedNote

	comments - Comments number
	date - Date when the note has been created in Unixtime
	id - Note ID
	owner_id - Note owner's ID
	read_comments - Read comments number
	title - Note title
	view_url - URL of the page with note preview
	"""
	comments = None
	date = None
	id = None
	owner_id = None
	read_comments = None
	title = None
	view_url = None


class WallCarouselBase(BaseModel):
	"""VK Object WallCarouselBase

	carousel_offset - Index of current carousel element
	"""
	carousel_offset = None


class WallCommentAttachment(BaseModel):
	"""VK Object WallCommentAttachment

	"""
	audio = None
	doc = None
	link = None
	market = None
	market_market_album = None
	note = None
	page = None
	photo = None
	sticker = None
	type = None
	video = None


class WallCommentAttachmentType(enum.Enum):
	"""VK Object WallCommentAttachmentType

	"""
	PHOTO = "photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	NOTE = "note"
	PAGE = "page"
	MARKET_MARKET_ALBUM = "market_market_album"
	MARKET = "market"
	STICKER = "sticker"


class WallGeo(BaseModel):
	"""VK Object WallGeo

	coordinates - Coordinates as string. <latitude> <longtitude>
	place - 
	showmap - Information whether a map is showed
	type - Place type
	"""
	coordinates = None
	place = None
	showmap = None
	type = None


class WallGraffiti(BaseModel):
	"""VK Object WallGraffiti

	id - Graffiti ID
	owner_id - Graffiti owner's ID
	photo_200 - URL of the preview image with 200 px in width
	photo_586 - URL of the preview image with 586 px in width
	"""
	id = None
	owner_id = None
	photo_200 = None
	photo_586 = None


class WallPostCopyright(BaseModel):
	"""VK Object WallPostCopyright

	"""
	id = None
	link = None
	name = None
	type = None


class WallPostSource(BaseModel):
	"""VK Object WallPostSource

	data - Additional data
	platform - Platform name
	type - 
	url - URL to an external site used to publish the post
	"""
	data = None
	platform = None
	type = None
	url = None


class WallPostSourceType(enum.Enum):
	"""VK Object WallPostSourceType

	"""
	VK = "vk"
	WIDGET = "widget"
	API = "api"
	RSS = "rss"
	SMS = "sms"
	MVK = "mvk"


class WallPostType(enum.Enum):
	"""VK Object WallPostType

	"""
	POST = "post"
	COPY = "copy"
	REPLY = "reply"
	POSTPONE = "postpone"
	SUGGEST = "suggest"


class WallPostedPhoto(BaseModel):
	"""VK Object WallPostedPhoto

	id - Photo ID
	owner_id - Photo owner's ID
	photo_130 - URL of the preview image with 130 px in width
	photo_604 - URL of the preview image with 604 px in width
	"""
	id = None
	owner_id = None
	photo_130 = None
	photo_604 = None


class WallVieWs(BaseModel):
	"""VK Object WallVieWs

	count - Count
	"""
	count = None


class WallWallComment(BaseModel):
	"""VK Object WallWallComment

	attachments - 
	date - Date when the comment has been added in Unixtime
	donut - 
	from_id - Author ID
	id - Comment ID
	likes - 
	real_offset - Real position of the comment
	reply_to_comment - Replied comment ID
	reply_to_user - Replied user ID
	text - Comment text
	thread - 
	post_id - 
	owner_id - 
	parents_stack - 
	deleted - 
	"""
	attachments = None
	date = None
	donut = None
	from_id = None
	id = None
	likes = None
	real_offset = None
	reply_to_comment = None
	reply_to_user = None
	text = None
	thread = None
	post_id = None
	owner_id = None
	parents_stack = None
	deleted = None


class WallWallCommentDonut(BaseModel):
	"""VK Object WallWallCommentDonut

	is_don - Means commentator is donator
	placeholder - 
	"""
	is_don = None
	placeholder = None


class WallWallCommentDonutPlaceholder(BaseModel):
	"""VK Object WallWallCommentDonutPlaceholder

	"""
	text = None


class WallWallpost(BaseModel):
	"""VK Object WallWallpost

	access_key - Access key to private object
	attachments - 
	copyright - Information about the source of the post
	date - Date of publishing in Unixtime
	edited - Date of editing in Unixtime
	from_id - Post author ID
	geo - 
	id - Post ID
	is_archived - Is post archived, only for post owners
	is_favorite - Information whether the post in favorites list
	likes - Count of likes
	owner_id - Wall owner's ID
	poster - 
	post_id - If post type 'reply', contains original post ID
	parents_stack - If post type 'reply', contains original parent IDs stack
	post_source - 
	post_type - 
	reposts - 
	signer_id - Post signer ID
	text - Post text
	views - Count of views
	"""
	access_key = None
	attachments = None
	copyright = None
	date = None
	edited = None
	from_id = None
	geo = None
	id = None
	is_archived = None
	is_favorite = None
	likes = None
	owner_id = None
	poster = None
	post_id = None
	parents_stack = None
	post_source = None
	post_type = None
	reposts = None
	signer_id = None
	text = None
	views = None


class WallWallpostAttachment(BaseModel):
	"""VK Object WallWallpostAttachment

	access_key - Access key for the audio
	album - 
	app - 
	audio - 
	doc - 
	event - 
	group - 
	graffiti - 
	link - 
	market - 
	market_album - 
	note - 
	page - 
	photo - 
	photos_list - 
	poll - 
	posted_photo - 
	type - 
	video - 
	"""
	access_key = None
	album = None
	app = None
	audio = None
	doc = None
	event = None
	group = None
	graffiti = None
	link = None
	market = None
	market_album = None
	note = None
	page = None
	photo = None
	photos_list = None
	poll = None
	posted_photo = None
	type = None
	video = None


class WallWallpostAttachmentType(enum.Enum):
	"""VK Object WallWallpostAttachmentType

	"""
	PHOTO = "photo"
	POSTED_PHOTO = "posted_photo"
	AUDIO = "audio"
	VIDEO = "video"
	DOC = "doc"
	LINK = "link"
	GRAFFITI = "graffiti"
	NOTE = "note"
	APP = "app"
	POLL = "poll"
	PAGE = "page"
	ALBUM = "album"
	PHOTOS_LIST = "photos_list"
	MARKET_MARKET_ALBUM = "market_market_album"
	MARKET = "market"
	EVENT = "event"


class WallWallpostCommentsDonut(BaseModel):
	"""VK Object WallWallpostCommentsDonut

	"""
	placeholder = None


class WallWallpostCommentsDonutPlaceholder(BaseModel):
	"""VK Object WallWallpostCommentsDonutPlaceholder

	"""
	text = None


class WallWallpostDonut(BaseModel):
	"""VK Object WallWallpostDonut

	is_donut - Post only for dons
	paid_duration - Value of this field need to pass in wall.post/edit in donut_paid_duration
	placeholder - If placeholder was respond, text and all attachments will be hidden
	can_publish_free_copy - Says whether group admin can post free copy of this donut post
	edit_mode - Says what user can edit in post about donut properties
	"""
	is_donut = None
	paid_duration = None
	placeholder = None
	can_publish_free_copy = None
	edit_mode = None


class WallWallpostDonutPlaceholder(BaseModel):
	"""VK Object WallWallpostDonutPlaceholder

	"""
	text = None


class WallWallpostFull(BaseModel):
	"""VK Object WallWallpostFull

	copy_history - 
	can_edit - Information whether current user can edit the post
	created_by - Post creator ID (if post still can be edited)
	can_delete - Information whether current user can delete the post
	can_pin - Information whether current user can pin the post
	donut - 
	is_pinned - Information whether the post is pinned
	comments - 
	marked_as_ads - Information whether the post is marked as ads
	short_text_rate - Preview length control parameter
	"""
	copy_history = None
	can_edit = None
	created_by = None
	can_delete = None
	can_pin = None
	donut = None
	is_pinned = None
	comments = None
	marked_as_ads = None
	short_text_rate = None


class WallWallpostToId(BaseModel):
	"""VK Object WallWallpostToId

	attachments - 
	comments - 
	copy_owner_id - ID of the source post owner
	copy_post_id - ID of the source post
	date - Date of publishing in Unixtime
	from_id - Post author ID
	geo - 
	id - Post ID
	is_favorite - Information whether the post in favorites list
	likes - 
	post_id - wall post ID (if comment)
	post_source - 
	post_type - 
	reposts - 
	signer_id - Post signer ID
	text - Post text
	to_id - Wall owner's ID
	"""
	attachments = None
	comments = None
	copy_owner_id = None
	copy_post_id = None
	date = None
	from_id = None
	geo = None
	id = None
	is_favorite = None
	likes = None
	post_id = None
	post_source = None
	post_type = None
	reposts = None
	signer_id = None
	text = None
	to_id = None


class WidgetsCommentMedia(BaseModel):
	"""VK Object WidgetsCommentMedia

	item_id - Media item ID
	owner_id - Media owner's ID
	thumb_src - URL of the preview image (type=photo only)
	type - 
	"""
	item_id = None
	owner_id = None
	thumb_src = None
	type = None


class WidgetsCommentMediaType(enum.Enum):
	"""VK Object WidgetsCommentMediaType

	"""
	AUDIO = "audio"
	PHOTO = "photo"
	VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
	"""VK Object WidgetsCommentReplies

	can_post - Information whether current user can comment the post
	count - Comments number
	replies - 
	"""
	can_post = None
	count = None
	replies = None


class WidgetsCommentRepliesItem(BaseModel):
	"""VK Object WidgetsCommentRepliesItem

	cid - Comment ID
	date - Date when the comment has been added in Unixtime
	likes - 
	text - Comment text
	uid - User ID
	user - 
	"""
	cid = None
	date = None
	likes = None
	text = None
	uid = None
	user = None


class WidgetsWidgetComment(BaseModel):
	"""VK Object WidgetsWidgetComment

	attachments - 
	can_delete - Information whether current user can delete the comment
	comments - 
	date - Date when the comment has been added in Unixtime
	from_id - Comment author ID
	id - Comment ID
	likes - 
	media - 
	post_source - 
	post_type - Post type
	reposts - 
	text - Comment text
	to_id - Wall owner
	user - 
	"""
	attachments = None
	can_delete = None
	comments = None
	date = None
	from_id = None
	id = None
	likes = None
	media = None
	post_source = None
	post_type = None
	reposts = None
	text = None
	to_id = None
	user = None


class WidgetsWidgetLikes(BaseModel):
	"""VK Object WidgetsWidgetLikes

	count - Likes number
	"""
	count = None


class WidgetsWidgetPage(BaseModel):
	"""VK Object WidgetsWidgetPage

	comments - 
	date - Date when widgets on the page has been initialized firstly in Unixtime
	description - Page description
	id - Page ID
	likes - 
	page_id - page_id parameter value
	photo - URL of the preview image
	title - Page title
	url - Page absolute URL
	"""
	comments = None
	date = None
	description = None
	id = None
	likes = None
	page_id = None
	photo = None
	title = None
	url = None
