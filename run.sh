echo 'Starting initial run ...'
python main.py
echo 'Finished initial run.'
echo 'Running cron ...'
crond -L /var/log/cron.log && tail -f /var/log/cron.log
