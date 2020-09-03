#!/bin/bash

#use this_file_name | bluetoothctl

echo -e 'power on\n'

sleep 2

echo -e 'scan on\n'

sleep 2

echo -e 'discoverable on\n'

sleep 2

echo -e 'pairable on\n'

sleep 2

echo -e 'pair 08:DF:1F:42:24:2B\n'

sleep 4

echo -e 'connect 08:DF:1F:42:24:2B\n'

sleep 5

echo -e 'quit\n'

