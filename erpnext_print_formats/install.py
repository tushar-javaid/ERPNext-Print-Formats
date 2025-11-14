import os
import frappe
from frappe.utils.file_manager import save_file


def after_install():
    upload_public_font()


def upload_public_font():
    """
    Automatically uploads Jameel-Noori-Nastaleeq.ttf into File doctype.
    - Makes file public
    - Prevents duplicate uploads
    - Logs all actions
    - Works even if reinstalling
    """
    app = "erpnext_print_formats"
    font_name = "Jameel-Noori-Nastaleeq.ttf"

    # Path: /apps/erpnext_print_formats/erpnext_print_formats/assets
    font_path = frappe.get_app_path(app, "assets", font_name)

    if not os.path.exists(font_path):
        frappe.log_error(
            f"Font '{font_name}' not found at {font_path}",
            "erpnext_print_formats: font missing"
        )
        return

    # Create public/files folder if missing
    public_files = frappe.get_site_path("public", "files")
    os.makedirs(public_files, exist_ok=True)

    # Skip if already uploaded
    existing = frappe.db.exists("File", {"file_name": font_name})
    if existing:
        frappe.logger("erpnext_print_formats").info(
            f"Font '{font_name}' already exists as File {existing}. Skipping."
        )
        return

    try:
        with open(font_path, "rb") as f:
            content = f.read()

        # Upload as PUBLIC file
        file_doc = save_file(
            file_name=font_name,
            content=content,
            folder="Home",
            is_private=0,         # PUBLIC
            content_type="font/ttf"
        )

        frappe.db.commit()

        frappe.logger("erpnext_print_formats").info(
            f"Font '{font_name}' uploaded successfully as File {file_doc.name}"
        )

    except Exception as e:
        frappe.log_error(
            message=str(e),
            title="erpnext_print_formats: font upload failed"
        )
