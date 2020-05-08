from magicdict import MagicDict
import json

# create a default order
mdorder = MagicDict().set_defaults(
    {
        '^price$': 0,
        '_address$': 'No such street, PO 000'
    }).set_defaults({'^items$': []}, do_copy=True)
mdorder['items']
mdorder['price']
mdorder['shipping_address']
mdorder['billing_address']

md = MagicDict().set_defaults(
    {'^[0-9]+$': mdorder}, do_copy=True).set_filter('^!')
md['customers']['foo'][1]['price'] = 15
md['customers']['foo'][1]['items'].append('notebook')
md['customers']['foo'][1]['shipping_address'] = 'FOO street'
md['customers']['foo'][1]['billing_address'] = 'FOO office'
md['customers']['foo'][1]['!notes'] = 'important notes'
md['customers']['foo'][2]  # use all defaults
md['customers']['!important customer'][1]['price'] = 25  # use default address
md['customers']['!important customer'][1]['items'].append('pen')
print(json.dumps(md, default=lambda o: o.data, indent=2))
print('\n-----important only:-----\n')
print(json.dumps(md.filter(), default=lambda o: o.data, indent=2))
print('\n-----items only:-----\n')
print(json.dumps(md.filter('^items$'), default=lambda o: o.data, indent=2))
