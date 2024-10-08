from regipy.plugins.system.safeboot_configuration import SafeBootConfigurationPlugin
from regipy_tests.validation.validation import ValidationCase


def test_safeboot_config_result(c: ValidationCase):
    assert {x["name"] for x in c.plugin_output["network"]} == {
        "volmgrx.sys",
        "PlugPlay",
        "NetBT",
        "{4D36E977-E325-11CE-BFC1-08002BE10318}",
        "mfefirek.sys",
        "SWPRV",
        "{4D36E965-E325-11CE-BFC1-08002BE10318}",
        "mfefire",
        "WudfPf",
        "Dhcp",
        "CryptSvc",
        "WudfSvc",
        "TabletInputService",
        "netprofm",
        "ndiscap",
        "mfevtp",
        "System Bus Extender",
        "NetDDEGroup",
        "{50DD5230-BA8A-11D1-BF5D-0000F805F530}",
        "MCODS",
        "Wlansvc",
        "mrxsmb20",
        "PNP_TDI",
        "nsiproxy.sys",
        "{745A17A0-74D3-11D0-B6FE-00A0C90F57DA}",
        "Messenger",
        "TrustedInstaller",
        "rdsessmgr",
        "{4D36E97D-E325-11CE-BFC1-08002BE10318}",
        "DnsCache",
        "{4D36E980-E325-11CE-BFC1-08002BE10318}",
        "dfsc",
        "RpcSs",
        "volmgr.sys",
        "LanmanServer",
        "sacsvr",
        "File system",
        "WinDefend",
        "McMPFSvc",
        "NTDS",
        "{4D36E973-E325-11CE-BFC1-08002BE10318}",
        "LmHosts",
        "DcomLaunch",
        "PNP Filter",
        "NlaSvc",
        "Power",
        "Base",
        "ProfSvc",
        "{71A27CDD-812A-11D0-BEC7-08002BE2092F}",
        "mfehidk.sys",
        "NetworkProvider",
        "mrxsmb",
        "NDIS Wrapper",
        "{4D36E96B-E325-11CE-BFC1-08002BE10318}",
        "{4D36E97B-E325-11CE-BFC1-08002BE10318}",
        "NDIS",
        "Network",
        "WudfRd",
        "{4D36E969-E325-11CE-BFC1-08002BE10318}",
        "VDS",
        "Boot Bus Extender",
        "{D48179BE-EC20-11D1-B6B8-00C04FA372A7}",
        "PolicyAgent",
        "{4D36E972-E325-11CE-BFC1-08002BE10318}",
        "vga.sys",
        "Primary disk",
        "LanmanWorkstation",
        "Ndisuio",
        "PCI Configuration",
        "Dot3Svc",
        "Streams Drivers",
        "vmms",
        "{4D36E96A-E325-11CE-BFC1-08002BE10318}",
        "{6BDD1FC1-810F-11D0-BEC7-08002BE2092F}",
        "{4D36E967-E325-11CE-BFC1-08002BE10318}",
        "TDI",
        "WinMgmt",
        "WudfUsbccidDriver",
        "Boot file system",
        "mfehidk",
        "Browser",
        "BFE",
        "VaultSvc",
        "RpcEptMapper",
        "NetBIOS",
        "vgasave.sys",
        "SharedAccess",
        "AFD",
        "{4D36E96F-E325-11CE-BFC1-08002BE10318}",
        "bowser",
        "MPSSvc",
        "rdpencdd.sys",
        "mrxsmb10",
        "{D94EE5D8-D189-4994-83D2-F68D7D41B0E6}",
        "KeyIso",
        "Netlogon",
        "Eaphost",
        "TBS",
        "AppMgmt",
        "IKEEXT",
        "NativeWifiP",
        "{4D36E974-E325-11CE-BFC1-08002BE10318}",
        "MPSDrv",
        "rdbss",
        "EventLog",
        "Tcpip",
        "EFS",
        "mfefirek",
        "SCardSvr",
        "sermouse.sys",
        "{4D36E975-E325-11CE-BFC1-08002BE10318}",
        "Filter",
        "AppInfo",
        "NetBIOSGroup",
        "{533C5B84-EC70-11D2-9505-00C04F79DEAF}",
        "ipnat.sys",
        "SCSI Class",
        "NetMan",
        "{36FC9E60-C465-11CF-8056-444553540000}",
        "HelpSvc",
        "Nsi",
    }
    assert {x["name"] for x in c.plugin_output["minimal"]} == {
        "vga.sys",
        "{4D36E97D-E325-11CE-BFC1-08002BE10318}",
        "{4D36E980-E325-11CE-BFC1-08002BE10318}",
        "volmgrx.sys",
        "Primary disk",
        "RpcSs",
        "volmgr.sys",
        "PlugPlay",
        "sacsvr",
        "File system",
        "WinDefend",
        "{D94EE5D8-D189-4994-83D2-F68D7D41B0E6}",
        "PCI Configuration",
        "KeyIso",
        "NTDS",
        "Netlogon",
        "vmms",
        "{4D36E977-E325-11CE-BFC1-08002BE10318}",
        "{4D36E96A-E325-11CE-BFC1-08002BE10318}",
        "SWPRV",
        "DcomLaunch",
        "PNP Filter",
        "Power",
        "{4D36E965-E325-11CE-BFC1-08002BE10318}",
        "Base",
        "AppMgmt",
        "TBS",
        "{6BDD1FC1-810F-11D0-BEC7-08002BE2092F}",
        "ProfSvc",
        "{71A27CDD-812A-11D0-BEC7-08002BE2092F}",
        "WudfPf",
        "{4D36E967-E325-11CE-BFC1-08002BE10318}",
        "CryptSvc",
        "WudfSvc",
        "WinMgmt",
        "TabletInputService",
        "{4D36E96B-E325-11CE-BFC1-08002BE10318}",
        "Boot file system",
        "System Bus Extender",
        "EventLog",
        "{4D36E97B-E325-11CE-BFC1-08002BE10318}",
        "MCODS",
        "EFS",
        "sermouse.sys",
        "WudfRd",
        "Filter",
        "RpcEptMapper",
        "AppInfo",
        "vgasave.sys",
        "{4D36E969-E325-11CE-BFC1-08002BE10318}",
        "{533C5B84-EC70-11D2-9505-00C04F79DEAF}",
        "VDS",
        "{745A17A0-74D3-11D0-B6FE-00A0C90F57DA}",
        "SCSI Class",
        "Boot Bus Extender",
        "{D48179BE-EC20-11D1-B6B8-00C04FA372A7}",
        "{36FC9E60-C465-11CF-8056-444553540000}",
        "HelpSvc",
        "TrustedInstaller",
        "{4D36E96F-E325-11CE-BFC1-08002BE10318}",
    }


class SafeBootConfigurationPluginValidationCase(ValidationCase):
    plugin = SafeBootConfigurationPlugin
    test_hive_file_name = "SYSTEM.xz"
    custom_test = test_safeboot_config_result
    expected_entries_count = 2
