import re, sys
ROOT = '/home/nctadmin/bench1098/iv-branded/linphone-android-iv'
def edit(path, subs, must=True):
    p = f'{ROOT}/{path}'
    s = open(p).read()
    for old, new in subs:
        if old not in s:
            if must: sys.exit(f'PATTERN NOT FOUND in {path}: {old[:60]}')
            continue
        s = s.replace(old, new, 1)
    open(p,'w').write(s)
    print('edited', path)

# 1. applicationId
edit('app/build.gradle.kts', [('val packageName = "org.linphone"','val packageName = "com.getintegrityvoice.softphone"')])
# 2. app name
edit('app/src/main/res/values/strings.xml', [('<!ENTITY appName "Linphone">','<!ENTITY appName "IntegrityVoice">')])
# 3. brand colors: primary scale -> Integrity navy / pale navy tint
edit('app/src/main/res/values/colors.xml', [
    ('<color name="orange_main_100">#FFEACB</color>','<color name="orange_main_100">#D9E6F5</color>'),
    ('<color name="orange_main_500">#FF5E00</color>','<color name="orange_main_500">#132C56</color>'),
])
# 4. adaptive icon background -> white (logo on white)
for f in ('ic_launcher.xml','ic_launcher_round.xml'):
    edit(f'app/src/main/res/mipmap-anydpi/{f}', [('<background android:drawable="@color/orange_main_500" />','<background android:drawable="@color/bc_white" />')])
# 5. linphonerc defaults: brand contact, domain prefill, assistant defaults
p = f'{ROOT}/app/src/main/assets/linphonerc_default'
s = open(p).read()
s = s.replace('contact="Linphone Android" <sip:linphone.android@unknown-host>',
              'contact="IntegrityVoice" <sip:integrityvoice.android@unknown-host>',1)
s = s.replace('contacts_filter=sip.linphone.org','contacts_filter=pbx.getintegrityvoice.com',1)
s = s.replace('[ui]\ncontacts_filter', '[ui]\nassistant_third_party_sip_account_domain=pbx.getintegrityvoice.com\nassistant_third_party_sip_account_transport=udp\nassistant_go_directly_to_third_party_sip_account_login=1\ncontacts_filter',1)
s = s.replace('[app]\ntunnel=disabled', '[app]\ndefault_domain=pbx.getintegrityvoice.com\ntunnel=disabled',1)
open(p,'w').write(s)
print('edited app/src/main/assets/linphonerc_default')
print('ALL BRAND EDITS APPLIED')
