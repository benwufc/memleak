a=1
while [ 1 ]
do
echo "====test time=$a===" > /dev/console
wifi up
sleep 50
wifi down
sleep 10
sync
echo 1 > /proc/net/skb_recycler/flush
echo 3 > /proc/sys/vm/drop_caches
echo "====test time=$a=infomation==" > /dev/console
echo "==== meminfo ===="
cat /proc/meminfo
echo "==== slabinfo ===="
cat /proc/slabinfo 
echo "==== kmemleak ===="
echo scan > /sys/kernel/debug/kmemleak
cat /sys/kernel/debug/kmemleak
echo "==== ps ===="
ps

set serverip 192.168.1.10
sleep 10
a=$((a+1))
done
