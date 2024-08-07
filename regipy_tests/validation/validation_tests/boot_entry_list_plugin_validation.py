from regipy.plugins.bcd.boot_entry_list import BootEntryListPlugin
from regipy_tests.validation.validation import ValidationCase


class BootEntryListPluginValidationCase(ValidationCase):
    plugin = BootEntryListPlugin
    test_hive_file_name = "BCD.xz"
    exact_expected_result = [
        {
            "guid": "{733b62de-f608-11eb-825c-c112f60133ab}",
            "type": "0x101FFFFF",
            "name": "Linux Boot Manager",
            "gpt_disk": "376e5397-7d1f-4e4f-a668-5a62c1269e60",
            "gpt_partition": "24e0e103-9bc2-477e-a5e2-3e42d2bb134f",
            "image_path": "\\EFI\\systemd\\systemd-bootx64.efi",
            "timestamp": "2021-08-09T02:13:30.992594+00:00",
        },
        {
            "guid": "{733b62e2-f608-11eb-825c-c112f60133ab}",
            "type": "0x101FFFFF",
            "name": "UEFI OS",
            "gpt_disk": "376e5397-7d1f-4e4f-a668-5a62c1269e60",
            "gpt_partition": "24e0e103-9bc2-477e-a5e2-3e42d2bb134f",
            "image_path": "\\EFI\\BOOT\\BOOTX64.EFI",
            "timestamp": "2021-08-09T02:13:30.992594+00:00",
        },
        {
            "guid": "{733b62e3-f608-11eb-825c-c112f60133ab}",
            "type": "0x101FFFFF",
            "name": "Windows Boot Manager",
            "gpt_disk": "376e5397-7d1f-4e4f-a668-5a62c1269e60",
            "gpt_partition": "24e0e103-9bc2-477e-a5e2-3e42d2bb134f",
            "image_path": "\\EFI\\Microsoft\\Boot\\bootmgfw.efi",
            "timestamp": "2021-08-09T02:13:30.992594+00:00",
        },
        {
            "guid": "{733b62e4-f608-11eb-825c-c112f60133ab}",
            "type": "0x10200004",
            "name": "Windows Resume Application",
            "gpt_disk": "0b2394a9-095e-487d-8d48-719ecd4d78ca",
            "gpt_partition": "8e0f2c38-e4ea-47ba-b7fc-9d8c74dccf0b",
            "image_path": "\\Windows\\system32\\winresume.efi",
            "timestamp": "2021-08-09T02:13:30.992594+00:00",
        },
        {
            "guid": "{733b62e5-f608-11eb-825c-c112f60133ab}",
            "type": "0x10200003",
            "name": "Windows 10",
            "gpt_disk": "0b2394a9-095e-487d-8d48-719ecd4d78ca",
            "gpt_partition": "8e0f2c38-e4ea-47ba-b7fc-9d8c74dccf0b",
            "image_path": "\\Windows\\system32\\winload.efi",
            "timestamp": "2021-08-09T02:13:30.992594+00:00",
        },
        {
            "guid": "{733b62e6-f608-11eb-825c-c112f60133ab}",
            "type": "0x10200003",
            "name": "Windows Recovery Environment",
            "gpt_disk": "00000001-0090-0000-0500-000006000000",
            "gpt_partition": "00000003-0000-0000-0000-000000000000",
            "image_path": "\\windows\\system32\\winload.efi",
            "timestamp": "2021-08-09T02:13:30.976970+00:00",
        },
        {
            "guid": "{9dea862c-5cdd-4e70-acc1-f32b344d4795}",
            "type": "0x10100002",
            "name": "Windows Boot Manager",
            "gpt_disk": "0b2394a9-095e-487d-8d48-719ecd4d78ca",
            "gpt_partition": "36be3955-63bf-4068-a6ab-00195cca3a22",
            "image_path": "\\EFI\\Microsoft\\Boot\\bootmgfw.efi",
            "timestamp": "2021-08-09T02:13:30.992594+00:00",
        },
        {
            "guid": "{b2721d73-1db4-4c62-bf78-c548a880142d}",
            "type": "0x10200005",
            "name": "Windows Memory Diagnostic",
            "gpt_disk": "0b2394a9-095e-487d-8d48-719ecd4d78ca",
            "gpt_partition": "36be3955-63bf-4068-a6ab-00195cca3a22",
            "image_path": "\\EFI\\Microsoft\\Boot\\memtest.efi",
            "timestamp": "2021-08-09T02:13:30.976970+00:00",
        },
    ]
