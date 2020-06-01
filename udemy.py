import urllib3
import requests
import browser_cookie3
from pathlib import Path
import time
import sys
import datetime
import argparse
from __colors import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sub_course(courseid, cookies, head):
    r2 = requests.get('https://www.udemy.com/api-2.0/course-landing-components/' + str(courseid) + '/me/?components=purchase', headers=head, verify=False, cookies=cookies)
    js = r2.json()
    if(js['purchase']['data']['is_valid_student'] == False):

        r = requests.get('https://www.udemy.com/course/subscribe/?courseId=' + str(courseid), headers=head, verify=False, cookies=cookies)
        
        rt = {
            'is_valid_student': '1'
        }
        return rt
    else:
        rt = {
            'detail': js['purchase']['data']['purchase_date']
        }
        return rt

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

def find_courses(limit, page, head):
    url3 = 'https://www.udemy.com/api-2.0/courses/?fields[course]=title,headline,num_published_lectures,num_subscribers,content_info,num_reviews,rating,original_price_text,is_paid,is_available_on_google_app,promo_asset,visible_instructors,image_750x422,image_480x270,image_240x135,google_in_app_purchase_price_text,is_user_subscribed,price_detail,google_in_app_price_detail,google_in_app_product_id,features,discount,campaign,last_update_date,has_closed_caption,caption_languages,badges&fields[user]=title,job_title,image_100x100&fields[asset]=title,asset_type,length&search=free%20courses&src=sac&page='+ str(page) +'&page_size=' + str(limit) + '&locale=en_US'

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
        '-p', '--page',\
        dest='page',\
        type=str,\
        help="Page No. to start from",metavar='')
    
    args = parser.parse_args()
    cookies = browser_cookie3.chrome(domain_name='www.udemy.com')
    my_cookies = requests.utils.dict_from_cookiejar(cookies)
    try:
        access_token = my_cookies['access_token']
        csrftoken = my_cookies['csrftoken']

    except Exception as e:
        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Make sure you are logged in to udemy.com in chrome browser')
        access_token = ''
        exit()
    
    if access_token != '':
        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Auto Login Successful! \n')
        try:
            if args.page:
                page = int(args.page)
            else:
                page = 1
        except:
            page = 1

        # cookie_v2 = gen_cookies()

        head = {
            'authorization': 'Bearer ' + access_token,
            'accept': 'application/json, text/plain, */*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'x-csrftoken': csrftoken,
            'x-udemy-authorization': 'Bearer ' + access_token,
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.udemy.com',
            'referer': 'https://www.udemy.com/'
        }
        # if cookies_file.exists():
        #     try:
        #         fp = open(cookies_file, 'r')
        #         token1 = fp.read()
        #         tk = token1.split('||')
        #         token = tk[0]
        #         name = tk[1]
        #         user_id = tk[2]

        #     except:
        #         print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + ' Wrong Format of Cookies File\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + ']  Right Format - access_token||your name||ud_cache_user')
        # else:
        #     print(args.cookies + ' File Not Found')
        #     token = ''
        
        subscribe_any = ''
        limit = 50
        while subscribe_any != 'q':
            print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + ']    PAGE - '+ str(page))
            js1 = find_courses(limit, page, head)
            try:
                total_courses = js1['count']
                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fb + '   Total Courses: ' + bm + str(total_courses) + '\n')
                time.sleep(1)
                for i, items in enumerate(js1['results'], start=1):
                    if items['is_paid'] == False:
                        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '][' + fm + sb + '*' + fc + sd + '] ' + fr + '  '+ str(i), fy + ' '+ items['title']) 
                subscribe_any = input('\n[*]   Input "y" to subscribe any course, Input "n" To Load More Courses OR input "all" to subscribe all courses from all pages(automatically): ')

                if subscribe_any == 'y':
                    input_id = int(input('\n[*]   Enter ID of Course ex - 1 or 2 or 3 ... OR Input 00 To Subscribe All Courses on Page '+str(page)+': '))
                    # print(input_id)
                    if input_id == 00:
                        for p in range(limit):
                            sub_js = sub_course(js1['results'][p]['id'], cookies, head)
                            try:
                                if sub_js['is_valid_student'] == '1':
                                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + '     Successfully Subscribed')
                                    # time.sleep(1)
                            except:
                                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + '     ' + sub_js['detail'])
                                # time.sleep(1)
                        page += 1
                    
                    else:
                        sub_js = sub_course(js1['results'][input_id-1]['id'], cookies, head)
                    
                        try:
                            if sub_js['is_valid_student'] == '1':
                                print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + ' Successfully Subscribed')
                                time.sleep(5)
                        except:
                            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + ' ' + sub_js['detail'])
                            time.sleep(5)
                elif subscribe_any == 'all':
                    subscribed = 0
                    for d in range(5000):
                        js4 = find_courses(limit, page, head)
                        print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + ']    PAGE - '+ str(page) + '\n')

                        time.sleep(1)
                        for i, items in enumerate(js4['results'], start=1):
                            if items['is_paid'] == False:
                                sub_js = sub_course(items['id'], cookies, head)
                                try:
                                    if sub_js['is_valid_student'] == '1':
                                        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + ' Successfully Subscribed -', fy + ' ' +items['title'])
                                        subscribed += 1
                                        # time.sleep(1)
                                except:
                                    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + sub_js['detail'] + ' -', fy + ' ' + items['title'])
                                    # time.sleep(1)
                        if len(js4['results']) < limit-1:
                            sys.exit('\nCompleted!!')
                        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fb + '   Total Courses Subscribed - ' + bm + str(subscribed))
                        page = page + 1
                    
                else:
                    if subscribe_any == 'n':
                        page += 1

            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                print('Unknown Error')
    else:
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + ' Make sure you are logged into udemy.com in chrome browser')

if __name__ == '__main__':
    main()