data = [{
    "asset_id": "2d24ce8afdeea7ba580c4437cb6df624",
    "item": "013601DB26984CB74BCCD767F1F4BC89",
    "type": "md5",
    "handle_state": "0"
}, {
    "asset_id": "2381545f4e96625daecbd9baad95b725",
    "item": "89739BC1E0E1B9E92D47AA38F0C8B1EF",
    "type": "md5",
    "handle_state": "0"
}, {
    "asset_id": "2d24ce8afdeea7ba580c4437cb6df624",
    "item": "89739BC1E0E1B9E92D47AA38F0C8B1EF",
    "type": "md5",
    "handle_state": "0"
}]
def check_data(data):
    items = []
    ids = []
    for d in data:
        if len(items) == 0:
            items.append(d['item'])
            ids.append({d['item']: [d['asset_id']]})
        else:
            if d['item'] in items:
                for i in ids:
                    if d['item'] in i.keys():
                        i[d['item']].append(d['asset_id'])
            else:
                items.append(d['item'])
                ids.append({d['item']: [d['asset_id']]})
    lists = []
    for i in items:
        ids2 = []
        for d in ids:
            if i in d.keys():
                ids2 = d[i]
                break
        lists.append({
            "asset_id": ','.join(ids2),
            "item": i,
            "type": "md5",
            "handle_state": "0"
        })
    return lists


print(check_data(data))
