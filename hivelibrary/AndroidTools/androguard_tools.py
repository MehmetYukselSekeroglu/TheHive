from androguard.core.apk import *
from androguard.util import set_log


def get_information_standard(apk_path:str) -> list:
    try:
        set_log("CRITICAL")
        targetApk = APK(apk_path)
        
        apk_appname = targetApk.get_app_name()
        apk_packageName = targetApk.get_package()
        apk_targetSdk = targetApk.get_target_sdk_version()
        apk_minSdk = targetApk.get_min_sdk_version()
        apk_maxSdk = targetApk.get_max_sdk_version()
        apk_internalVersion = targetApk.get_androidversion_code()
        apk_displayedVersion = targetApk.get_androidversion_name()
        apk_permissions = targetApk.get_permissions()
        apk_services = targetApk.get_services()
        apk_v1_issigned = targetApk.is_signed_v1()
        apk_v2_issigned = targetApk.is_signed_v2()
        apk_v3_issigned = targetApk.is_signed_v3()
        included_files = targetApk.get_files()
        included_librarys = targetApk.get_libraries()
        
        return [True, 
            apk_appname,
            apk_packageName,
            apk_targetSdk,
            apk_minSdk,
            apk_maxSdk,
            apk_internalVersion,
            apk_displayedVersion,
            apk_permissions,
            apk_services,
            apk_v1_issigned,
            apk_v2_issigned,
            apk_v3_issigned,
            included_librarys,
            included_files
            ]            
    
    except Exception as err:
        return [False, err]
    
    

if __name__ == "__main__":
    import sys
    
    apkfile  = sys.argv[1]
    data = get_information_standard(apk_path=apkfile)
    
    for a in data:
        print(a)
    
    
    
    