app_name = "zatca_emkan"
app_title = "Zatca Emkan"
app_publisher = "info@finbyz.tech"
app_description = "Zatca emkan"
app_email = "info@finbyz.tech"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "zatca_emkan",
# 		"logo": "/assets/zatca_emkan/logo.png",
# 		"title": "Zatca Emkan",
# 		"route": "/zatca_emkan",
# 		"has_permission": "zatca_emkan.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zatca_emkan/css/zatca_emkan.css"
# app_include_js = "/assets/zatca_emkan/js/zatca_emkan.js"

# include js, css files in header of web template
# web_include_css = "/assets/zatca_emkan/css/zatca_emkan.css"
# web_include_js = "/assets/zatca_emkan/js/zatca_emkan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "zatca_emkan/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "zatca_emkan/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "zatca_emkan.utils.jinja_methods",
# 	"filters": "zatca_emkan.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "zatca_emkan.install.before_install"
# after_install = "zatca_emkan.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "zatca_emkan.uninstall.before_uninstall"
# after_uninstall = "zatca_emkan.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "zatca_emkan.utils.before_app_install"
# after_app_install = "zatca_emkan.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "zatca_emkan.utils.before_app_uninstall"
# after_app_uninstall = "zatca_emkan.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zatca_emkan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"on_submit": "zatca_emkan.zatca_emkan.doc_events.sales_invoice.after_submit",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zatca_emkan.tasks.all"
# 	],
# 	"daily": [
# 		"zatca_emkan.tasks.daily"
# 	],
# 	"hourly": [
# 		"zatca_emkan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zatca_emkan.tasks.weekly"
# 	],
# 	"monthly": [
# 		"zatca_emkan.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "zatca_emkan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zatca_emkan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "zatca_emkan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["zatca_emkan.utils.before_request"]
# after_request = ["zatca_emkan.utils.after_request"]

# Job Events
# ----------
# before_job = ["zatca_emkan.utils.before_job"]
# after_job = ["zatca_emkan.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"zatca_emkan.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

import ksa_compliance.standard_doctypes.sales_invoice
from zatca_emkan.zatca_emkan.override.sales_invoice import create_sales_invoice_additional_fields_doctype as csiafd

ksa_compliance.standard_doctypes.sales_invoice.create_sales_invoice_additional_fields_doctype = csiafd


fixtures = [
    {
        "dt": "Custom Field",
        "filters": {"module": ["in", ["Zatca Emkan"]]},
    },
]