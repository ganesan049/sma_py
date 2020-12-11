//@version=2
// @author LazyBear
//
// If you use this code in its original/modified form, do drop me a note. 
//
strategy("MACD + SMA 200 Strategy (by ChartArt)", shorttitle="CA_-_MACD_SMA_strategy", overlay=true)
// study(title="WaveTrend [LazyBear]", shorttitle="WT_LB")
n1 = input(10, "Channel Length")
n2 = input(21, "Average Length")
obLevel1 = input(60, "Over Bought Level 1")
obLevel2 = input(53, "Over Bought Level 2")
osLevel1 = input(-60, "Over Sold Level 1")
osLevel2 = input(-53, "Over Sold Level 2")
 
ap = hlc3
esa = ema(ap, n1)
d = ema(abs(ap - esa), n1)
ci = (ap - esa) / (0.015 * d)
tci = ema(ci, n2)
 
wt1 = tci
wt2 = sma(wt1,4)

plot(0, color=gray)
plot(obLevel1, color=red)
plot(osLevel1, color=green)
plot(obLevel2, color=red, style=3)
plot(osLevel2, color=green, style=3)

plot(wt1, color=green)
plot(wt2, color=red, style=3)
plot(wt1-wt2, color=blue, style=area, transp=80)

macd_IsAbove = (wt1 >= wt2)
macd_IsBelow = wt1 <= wt2
macd_color = macd_IsAbove and wt1 < 0 ? lime : (wt2 > 0) ? red : na
plot(cross(wt1,wt2)?wt2:na,title="Cross", style=circles, linewidth=4, color=macd_color)
is_call = macd_IsAbove and cross(wt1,wt2) and wt1 < -10
is_put = macd_IsBelow and cross(wt1,wt2) and wt2 > 0
plotshape(is_call ? 1 : na, title="BUY ARROW", color=green, text="*buy*", style=shape.arrowup, location=location.absolute)
plotshape(is_put ? -1 : na, title="SELL ARROW", color=red, text="*sell*", style=shape.arrowdown, location=location.absolute)
