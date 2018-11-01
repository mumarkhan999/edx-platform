from openedx.features.caliper_tracking.transformers.bookmark_transformers import edx_bookmark_listed
from openedx.features.caliper_tracking.transformers.navigation_transformers import edx_ui_lms_link_clicked
from openedx.features.caliper_tracking.transformers.enrollment_transformers import (
    edx_course_enrollment_activated,
    edx_course_enrollment_mode_changed,
    edx_course_enrollment_deactivated,
    edx_course_enrollment_upgrade_clicked
)

"""
Mapping of events to their transformer functions
"""

EVENT_MAPPING = {
    'edx.bookmark.listed': edx_bookmark_listed,
    'edx.ui.lms.link_clicked': edx_ui_lms_link_clicked,
    'edx.course.enrollment.activated': edx_course_enrollment_activated,
    'edx.course.enrollment.deactivated': edx_course_enrollment_deactivated,
    'edx.course.enrollment.mode_changed': edx_course_enrollment_mode_changed,
    'edx.course.enrollment.upgrade.clicked': edx_course_enrollment_upgrade_clicked,
}
