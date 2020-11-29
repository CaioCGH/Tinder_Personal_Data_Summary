import json
import dateutil.parser


def days_between(d1, d2):
    d1 = dateutil.parser.parse(d1)
    d2 = dateutil.parser.parse(d2)
    return abs((d2 - d1).days)

def usage_report(data, usage_field):
    total = 0
    max_day = ""
    max = 0

    for k, v in data['Usage'][usage_field].items():
        total += v
        if v > max:
            max = v
            max_day = k
    report = {
        "total": total,
        "max_day": max_day,
        "max": max
    }
    return report

def average(number, days):
    return '%.3f'%(number/days)

def longest_sent_message(data):
    message = ""
    length = 0
    date = ""
    for msgs in data['Messages']:
        for m in msgs['messages']:
            if isinstance(m, dict) and length < len(m['message']):
                length = len(m['message'])
                message = m['message']
                date = m['sent_date']
    return {
        'message': message,
        'date': date
    }
with open('data.json') as f:
  data = json.load(f)

# stri = json.dumps(data, indent=4,ensure_ascii=False).encode('utf8')
# f = open("demofile2.json", "w")
# f.write(stri)
# f.close()
summary = {}
fields = ['app_opens', 'swipes_likes', 'swipes_passes', 'matches', 'messages_sent', 'messages_received']
for field in fields:
    summary[field] = usage_report(data, field)

days_since_creation = days_between(data['User']['active_time'], data['User']['create_date'])
longest_message = longest_sent_message(data)
my_summary = {
    'create_date': data['User']['create_date'],
    'days_since_creation': days_since_creation,
    'app_opens':{
        'total': summary['app_opens']['total'],
        'average_per_dar': average(summary['app_opens']['total'],days_since_creation),
        'max': summary['app_opens']['max'],
        'max_day': summary['app_opens']['max_day']
    },
    'swipes_likes':{
        'total': summary['swipes_likes']['total'],
        'average_per_day': average(summary['swipes_likes']['total'],days_since_creation),
        'max': summary['swipes_likes']['max'],
        'max_day': summary['swipes_likes']['max_day']
    },
    'swipes_passes':{
        'total': summary['swipes_passes']['total'],
        'average_per_day': average(summary['swipes_passes']['total'],days_since_creation),
        'max': summary['swipes_passes']['max'],
        'max_day': summary['swipes_passes']['max_day']
    },
    'matches':{
        'total': summary['matches']['total'],
        'average_per_day': average(summary['matches']['total'],days_since_creation),
        'max': summary['matches']['max'],
        'max_day': summary['matches']['max_day']
    },
    'messages_sent':{
        'total': summary['messages_sent']['total'],
        'average_per_day': average(summary['messages_sent']['total'],days_since_creation),
        'max': summary['messages_sent']['max'],
        'max_day': summary['messages_sent']['max_day']
    },
    'messages_received':{
        'total': summary['messages_received']['total'],
        'average_per_day': average(summary['messages_received']['total'],days_since_creation),
        'max': summary['messages_received']['max'],
        'max_day': summary['messages_received']['max_day']
    },
    'other_stats':{
        'Match percent rate': "{:.2%}".format(summary['matches']['total']/summary['swipes_likes']['total']),
        'Swipe like over all swipes': "{:.2%}".format(summary['swipes_likes']['total']/(summary['swipes_likes']['total'] + summary['swipes_passes']['total'])),
        'Swipe pass over all swipes': "{:.2%}".format(summary['swipes_passes']['total']/(summary['swipes_likes']['total'] + summary['swipes_passes']['total'])),
        'Messages sent over all messages': "{:.2%}".format(summary['messages_sent']['total']/(summary['messages_sent']['total'] + summary['messages_received']['total'])),
        'Messages received over all messages': "{:.2%}".format(summary['messages_received']['total']/(summary['messages_sent']['total'] + summary['messages_received']['total'])),
        # 'longest_message': {
        #     'message': longest_message['message'],
        #     'date': longest_message['date']
        # }
    }
}

json_summary = json.dumps(my_summary, indent=2)

print(json_summary)

f = open("my_summary.json", "w")
f.write(str(json_summary))
f.close()

