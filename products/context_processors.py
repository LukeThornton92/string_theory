from datetime import datetime, timedelta

def estimated_shipping(request):
    """Calculates estimated shipping date, 7 business days"""
    today = datetime.today()
    shipping_date = today + timedelta(days=7)
    return {'estimated_shipping_date' : shipping_date.strftime('%d %b %y')}