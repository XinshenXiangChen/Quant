from scipy.stats import norm
import math

def ln(stock_price, strike_price):
    return math.log(stock_price / strike_price)

def d1(stock_price, strike_price, risk_free_rate, vol, time_maturity):
    numerator = ln(stock_price, strike_price) + (risk_free_rate +  (vol*vol*0.5))*time_maturity
    denominator = vol*math.sqrt(time_maturity)
    return numerator / denominator

def d2(D1, vol, time_maturity):
    return D1 - (vol * math.sqrt(time_maturity))


def prediction(stock_price, strike_price, risk_free_rate, vol, time_maturity):
    _d1 = d1(stock_price, strike_price, risk_free_rate, vol, time_maturity)
    _d2 = d2(_d1, vol, time_maturity)
    return norm.cdf(_d1)*stock_price + norm.cdf(_d2)*strike_price*math.exp(-risk_free_rate*time_maturity)