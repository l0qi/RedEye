import shodan 
import time
import datetime
import os
import core.banner



core.banner.menu()
query = input('[query]: ')
shodan_key = 'RwhzAhS33ZTwpx8Q9hxAP5ZWxQdsBf1q'
date = datetime.datetime.today().strftime("%H.%M.%S-%d-%m")
api = shodan.Shodan(shodan_key)


if not os.path.exists('logs'):
    os.mkdir('logs')



def main():
    global results 

    try:
        time.sleep(1)
        results = api.search(query)
        print('[+] Starting search IP')

        for result in results['matches']:
            print(result['ip_str'])
            with open('logs/result.txt', 'a') as file:
                file.write('[TIME]: ' + date + ' ' + '[IP]: ' + result['ip_str'] + '\n')

    except KeyboardInterrupt:
        print('\n[!] (Ctrl + C) detected.. Stopping...')
        
    except shodan.APIError as e:
        print(e)


if __name__ == '__main__':
    main()
        