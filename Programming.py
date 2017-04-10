import urllib2;

request = urllib2.Request('http://www.wechall.net/challenge/training/programming1/index.php?action=request');

request.add_header('Cookie','WC=9372012-22804-3OpFOjpSoCPtXePu');

response = urllib2.urlopen(request);

message = response.read();

request = urllib2.Request('http://www.wechall.net/challenge/training/programming1/index.php?answer=%s' % message);

request.add_header('Cookie','WC=7326764-10727-GO6vlEtF1gaDd9dS');

response = urllib2.urlopen(request);

print response.read();