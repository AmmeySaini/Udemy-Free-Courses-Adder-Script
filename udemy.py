import urllib3
import requests
from pathlib import Path
import time
import sys
import datetime
import argparse
from __colors import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sub_course(id, cookie_v2, token, user_id):
    url5 = 'https://www.udemy.com/api-2.0/users/me/subscribed-courses/?fields[user]=title,image_100x100&fields[course]=title,headline,url,completion_ratio,num_published_lectures,image_480x270,image_240x135,favorite_time,archive_time,is_banned,is_taking_disabled,features,visible_instructors,last_accessed_time,sort_order,is_user_subscribed,is_wishlisted'

    headx = {
        'x-udemy-cache-device': 'tablet',
        'x-udemy-cache-campaign-code': '',
        'x-udemy-cache-logged-in': '0',
        'x-udemy-cache-modern-browser': '0',
        'x-udemy-cache-brand': 'INen_US',
        'x-udemy-cache-version': '1',
        'x-udemy-cache-language': 'en',
        'x-udemy-cache-marketplace-country': 'IN',
        'x-udemy-cache-user': '',
        'x-udemy-cache-price-country': 'IN',
        'x-udemy-cache-user': str(user_id),
        'cookie': cookie_v2,
        'x-udemy-bearer-token': token,
        'authorization': 'Bearer ' + token,
        'content-type': 'application/x-www-form-urlencoded',
        'accept-language': 'en_US',
        'x-mobile-visit-enabled': 'true',
        'x-version-name': '5.3.5',
        'x-client-name': 'Udemy-Android',
        'user-agent': 'okhttp/3.11.0 UdemyAndroid 5.3.5(222) (phone)'
    }

    data = 'course_id=' + str(id)

    r = requests.post(url=url5, headers=headx, data=data, verify=False)
    # print(r.text)

    return r.json()

def gen_cookies():

    url2 = 'https://www.udemy.com/api-2.0/visits/current/?fields[visit]=@default,visitor,country'

    head2 = {
        'x-mobile-visit-enabled': 'true'
    }

    r1 = requests.get(url=url2, headers=head2, verify=False)
    __udmy_2_v57r = r1.cookies['__udmy_2_v57r']
    # ud_cache_release = r1.cookies['ud_cache_release']
    ud_firstvisit = r1.cookies['ud_firstvisit']
    ud_rule_vars = r1.cookies['ud_rule_vars']
    __cfruid = r1.cookies['__cfruid']
    __cfduid = r1.cookies['__cfduid']
    evi = r1.cookies['evi']
    _pxhd = ''

    return '__udmy_2_v57r=' +__udmy_2_v57r+ '; ud_cache_release=; ud_firstvisit=' + ud_firstvisit + '; ud_rule_vars=' + ud_rule_vars + '; ud_cache_device=tablet; ud_cache_campaign_code=; seen=1; __cfruid=' + __cfruid + '; ud_cache_logged_in=0; __cfduid=' + __cfduid + '; ud_cache_modern_browser=0; ud_cache_brand=INen_US; evi=' + evi + '; _pxhd=' + _pxhd + '; ud_cache_version=1; ud_cache_language=en; ud_cache_marketplace_country=IN; ud_cache_user=; ud_cache_price_country=IN; __cfruid=' + __cfruid + '; __udmy_2_v57r=' + __udmy_2_v57r
def find_courses(limit, xy, head):
    url3 = 'https://www.udemy.com/api-2.0/courses/?fields[course]=title,headline,num_published_lectures,num_subscribers,content_info,num_reviews,rating,original_price_text,is_paid,is_available_on_google_app,promo_asset,visible_instructors,image_750x422,image_480x270,image_240x135,google_in_app_purchase_price_text,is_user_subscribed,price_detail,google_in_app_price_detail,google_in_app_product_id,features,discount,campaign,last_update_date,has_closed_caption,caption_languages,badges&fields[user]=title,job_title,image_100x100&fields[asset]=title,asset_type,length&search=free%20courses&src=sac&page='+ str(xy) +'&page_size=' + str(limit) + '&locale=en_US'

    r2 = requests.get(url3, headers=head, verify=False)
    return r2.json()
def main():
    version = '1.0'
    parser = argparse.ArgumentParser(description='', conflict_handler="resolve")
    general = parser.add_argument_group("General")
    general.add_argument(
        '-h', '--help',\
        action='help',\
        help="Shows the help.")
    general.add_argument(
        '-v', '--version',\
        action='version',\
        version=version,\
        help="Shows the version.")

    authentication = parser.add_argument_group("Authentication")
    authentication.add_argument(
        '-c', '--cookies',\
        dest='cookies',\
        type=str,\
        help="Cookies to authenticate",metavar='')
    authentication.add_argument(
        '-l', '--limit',\
        dest='Limit',\
        type=str,\
        help="Limit of courses per page",metavar='')
    
    args = parser.parse_args()
    if args.cookies:
        cookies_file = Path(args.cookies)

        cookie_v2 = gen_cookies()

        head = {
            'x-udemy-cache-device': 'tablet',
            'x-udemy-cache-campaign-code': '',
            'x-udemy-cache-logged-in': '0',
            'x-udemy-cache-modern-browser': '0',
            'x-udemy-cache-brand': 'INen_US',
            'x-udemy-cache-version': '1',
            'x-udemy-cache-language': 'en',
            'x-udemy-cache-marketplace-country': 'IN',
            'x-udemy-cache-user': '',
            'x-udemy-cache-price-country': 'IN',
            'cookie': cookie_v2,
            'content-type': 'application/x-www-form-urlencoded',
            'authorization': 'Basic YWQxMmVjYTljYmUxN2FmYWM2MjU5ZmU1ZDk4NDcxYTY6YTdjNjMwNjQ2MzA4ODI0YjIzMDFmZGI2MGVjZmQ4YTA5NDdlODJkNQ==',
            'accept-language': 'en_US',
            'accept-encoding': 'gzip',
            'x-mobile-visit-enabled': 'true',
            'x-mobile-client-id': 'Mzg69PT7RUQ6RjYUOP8DODc=',
            'x-version-name': '5.3.5',
            'x-client-name': 'Udemy-Android',
            'user-agent': 'okhttp/3.11.0 UdemyAndroid 5.3.5(222) (phone)'
        }

        # if my_file.exists():
        #     fp = open(my_file, 'r')
        #     token1 = fp.read()
        #     tk = token1.split('||')
        #     token = tk[0]
        #     name = tk[1]
        #     user_id = tk[2]
        # else:
        #     pwd = input('Enter Your Password: ')
        #     url = 'https://www.udemy.com/api-2.0/auth/udemy-auth/login/?fields[user]=title,image_100x100,is_fraudster,num_subscribed_courses,name,initials,has_instructor_intent,permissions,num_published_courses,access_token'

        #     dt = datetime.date.today()
        #     year = dt.year
        #     month = f'{dt.month:02d}'
        #     day = f'{dt.day:02d}'
                    
        #     payload = 'email=' + email +'&password=' + str(pwd) + '&upow=20200526AMRM'

        #     r = requests.post(url, headers=head, data=payload, verify=False)
        #     # print(r.text)

        if cookies_file.exists():
            try:
                fp = open(cookies_file, 'r')
                token1 = fp.read()
                tk = token1.split('||')
                token = tk[0]
                name = tk[1]
                user_id = tk[2]

            except:
                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + ' Wrong Format of Cookies File\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + ']  Right Format - access_token||your name||ud_cache_user')
        else:
            print(args.cookies + ' File Not Found')
            token = ''
        if token != '' :
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fm + ' Hello ' + sb + fb + name)
            subscribe_any = ''
            xy = 1
            limit = 50
            while subscribe_any != 'q':
                print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + ']    PAGE - '+ str(xy))
                js1 = find_courses(limit, xy, head)
                try:
                    total_courses = js1['count']
                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fb + '   Total Courses: ' + bm + str(total_courses) + '\n')
                    time.sleep(1)
                    for i, items in enumerate(js1['results'], start=1):
                        if items['is_paid'] == False:
                            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '][' + fm + sb + '*' + fc + sd + '] ' + fr + '  '+ str(i), fy + ' '+ items['title']) 
                    subscribe_any = input('\n[*]   Subscribe Any Course From Above ? (y/n), Input n To Load More Courses OR q To Quit: ')

                    if subscribe_any == 'y':
                        input_id = int(input('\n[*]   Enter ID of Course ex - 1 or 2 or 3 ... OR Input 00 To Subscribe All Courses on Page '+str(xy)+' OR Input 1111 To Automatically Add All Free Courses From All Pages: '))
                        # print(input_id)
                        if input_id == 00:
                            for p in range(limit):
                                sub_js = sub_course(js1['results'][p]['id'], cookie_v2, token, user_id)
                                try:
                                    if sub_js['_class'] == 'course':
                                        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + '     Successfully Subscribed')
                                        # time.sleep(1)
                                except:
                                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + '     ' + sub_js['detail'])
                                    # time.sleep(1)
                            xy += 1
                        elif input_id == 1111:
                            page = 1
                            subscribed = 0
                            for d in range(5000):
                                js4 = find_courses(limit, page, head)
                                print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + ']    PAGE - '+ str(page) + '\n')
                                # total_courses = js4['count']
                                # print('\nTotal Courses: ' + str(total_courses) + '\n')
                                time.sleep(1)
                                for i, items in enumerate(js4['results'], start=1):
                                    if items['is_paid'] == False:
                                        sub_js = sub_course(items['id'], cookie_v2, token, user_id)
                                        try:
                                            if sub_js['_class'] == 'course':
                                                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + ' Successfully Subscribed -', fy + ' ' +items['title'])
                                                subscribed += 1
                                                # time.sleep(1)
                                        except:
                                            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + sub_js['detail'] + ' -', fy + ' ' + items['title'])
                                            # time.sleep(1)
                                if len(js4['results']) < limit-1:
                                    sys.exit('Completed!!')
                                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fb + '   Total Courses Subscribed - ' + bm + str(subscribed))
                                page += 1
                        else:
                            sub_js = sub_course(js1['results'][input_id-1]['id'], cookie_v2, token, user_id)
                        
                        try:
                            if sub_js['_class'] == 'course':
                                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + ' Successfully Subscribed')
                                time.sleep(5)
                        except:
                            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + ' ' + sub_js['detail'])
                            time.sleep(5)
                    else:
                        if subscribe_any == 'n':
                            xy += 1

                except:
                    print("Oops!", sys.exc_info()[0], "occurred.")
                    print('Api Error')
    else:
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + ' Argument -c "cookies" is required')

if __name__ == '__main__':
    main()