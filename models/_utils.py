import models, datetime
    try:
        m.update_forward_refs(datetime=datetime)
    except Exception as e:
        print("f", m, e)