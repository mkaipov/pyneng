port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

dot1x_template = [
    "switchport mode access",
    "dot1x port-control auto",
    "dot1x guest-vlan 185",
    "dot1x auth-fail vlan 186"
]


def generate_access_config(interface_list, dot1x, psecurity=None):
    with open('sw_conf.txt', 'a+') as port_config:

        for intf in interface_list:
            port_config.write(f'interface {intf}\n',)
            if psecurity:
                for psec in psecurity:
                    port_config.write(f'{psec}\n')

            else:
                for command in dot1x:
                    port_config.write(f'{command}\n')


int_list = ['Gi1/1', 'Gi1/2', 'Gi1/3']

sw1 = generate_access_config(int_list, dot1x_template)
