from datetime import datetime, timedelta
import re
import subprocess


def get_key_details(key):
    """
    >>> get_key_details('ssh-dss AAAAB3NzaC1kc3MAAACBAJxrocPXtCxwgg5yvOc1NLFFz/Fql4+7sOgMOkwWO6pxpJ4bPZgzZ0B17/HGKxQaot3Nc7vzdkC3MBrDDbKrX4n9qB9yJBd0Kkr5X0K7SnBKU+7fbg+rloUdYE78LS6ap05+xlJ8dU918DnS3KqcT/YQQXaTLrt/2DUOM1qxCI1XAAAAFQCJXLN0vYx7SIYMQ0zhv9IUT5WhgQAAAIAT2new16avxvs56zU87t1QQe0qwbQEIUygWW6vqnc9Lo9aSf21sM5WAHTkEnTVyiFSI6K6Q6bD2OUMvS2oWaoariW8EFKzg7/pufmThG0oAxkloc3j8gMO2+xuw7yHzP2pd6xgosNkqivpsGT1PKo+vM6x8p9B6PvipHPqhgFHWQAAAIEAhgFE3+gfPpfDIhaPP5Adx4Hm0VO3xBgOtafvunv3kP54kvHuTaD2uLwgcdOsMedv1/tqhJddh4+9ibwhlKbxKLHrQIcGSHCIY/BoA4RnpSBlGoXEc2buLoZ9IwANCIa2mp19Q/v4wwLnTJHabdMkNCiUn8NPEiHUPjgIj1uoCgo= epsilon')
    {'algo': 'DSA', 'bits': 1024, 'sha256': 'o2DscHLwvUsYJ7a5eYgc2B4hQO4rf19u17W9Hh/H2h8', 'comment': 'epsilon', 'md5': 'f6:78:a7:9e:6b:41:dc:31:f4:39:12:5f:2b:0c:7a:11'}
    """
    process = subprocess.run(
        ['ssh-keygen', '-lEsha256', '-f-'],
        input=key.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    if process.returncode != 0:
        raise ValueError(process.stderr.decode('utf-8'))

    output = process.stdout.decode('utf-8').rstrip()
    m = re.match(
        r'^(?P<bits>\d+) SHA256:(?P<sha256>[^ ]+) (?P<comment>.*) \((?P<algo>.*)\)$',
        output
    )
    data = {
        'algo':  m.group('algo'),
        'bits': int(m.group('bits')),
        'sha256': m.group('sha256'),
        'comment': m.group('comment'),
    }

    process = subprocess.run(
        ['ssh-keygen', '-lEmd5', '-f-'],
        input=key.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    if process.returncode != 0:
        raise ValueError(process.stderr.decode('utf-8'))

    output = process.stdout.decode('utf-8').rstrip()
    m = re.match(
        r'^(?P<bits>\d+) MD5:(?P<md5>[a-f0-9:]+) (?P<comment>.*) \((?P<algo>.*)\)$',
        output
    )
    data['md5'] = m.group('md5')

    return data


def parse_log_line(line, year=None, allow_future_days=7):
    """
    >>> sorted(parse_log_line(
    ...     'Jan  1 2:34:56 heta sshd[4112]: Accepted publickey for localuser from 0.0.0.0 port 33980 ssh2: RSA f6:78:a7:9e:6b:41:dc:31:f4:39:12:5f:2b:0c:7a:11',
    ...     year=2019).items())
    [('algo', 'RSA'), ('datetime', datetime.datetime(2019, 1, 1, 2, 34, 56)), ('host', 'heta'), ('ip', '0.0.0.0'), ('md5', 'f6:78:a7:9e:6b:41:dc:31:f4:39:12:5f:2b:0c:7a:11'), ('user', 'localuser')]
    >>> sorted(parse_log_line(
    ...     'Jan  1 2:34:56 heta sshd[4112]: Accepted publickey for localuser from 0.0.0.0 port 33980 ssh2: RSA SHA256:9FLLdMdArtybwaoS45qtNZSmcBsr1pR2t8c9O+XODBw',
    ...     year=2019).items())
    [('algo', 'RSA'), ('datetime', datetime.datetime(2019, 1, 1, 2, 34, 56)), ('host', 'heta'), ('ip', '0.0.0.0'), ('sha256', '9FLLdMdArtybwaoS45qtNZSmcBsr1pR2t8c9O+XODBw'), ('user', 'localuser')]

    """
    logline_re = r'^(?P<time>\w{3}\s+\d+\s+\d?\d:\d\d:\d\d) (?P<host>\S+) .*: Accepted publickey for (?P<user>\S*) from (?P<ip>[\S]+) port .* ssh2: (?P<algo>\w+) ((?P<md5>[a-f0-9:]+)|SHA256:(?P<sha256>[a-zA-Z0-9+/]+))$'

    m = re.match(logline_re, line)
    if m is None:
        return None
    dt = datetime.strptime(m['time'], '%b %d %H:%M:%S')
    if year is not None:
        dt = dt.replace(year=year)
    else:
        now = datetime.now()
        dt = dt.replace(year=now.year)
        if (dt - now).days > allow_future_days:
            dt = dt.replace(year=dt.year - 1)

    data = {
        'datetime': dt,
        'host': m['host'],
        'user': m['user'],
        'ip': m['ip'],
        'algo': m['algo'],
    }
    if m['md5']:
        data['md5'] = m['md5']
    if m['sha256']:
        data['sha256'] = m['sha256']

    return data
