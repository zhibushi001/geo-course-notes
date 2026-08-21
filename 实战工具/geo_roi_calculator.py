#!/usr/bin/env python3
"""
GEO ROI 估算器 v1.0
计算做 GEO 优化能带来多少投资回报

用法:
  python geo_roi_calculator.py
  # 交互式输入参数
"""
import sys
import argparse


def calculate_roi(
    current_monthly_traffic=10000,
    current_conversion_rate=0.02,
    avg_order_value=500,
    geo_investment_monthly=5000,
    geo_boost_factor=1.3,  # GEO 优化带来的流量提升(1.3 = +30%)
    conversion_rate_lift=0.005,  # GEO 提升的转化率
):
    """计算 GEO 投资回报"""
    
    # 现状
    current_conversions = current_monthly_traffic * current_conversion_rate
    current_revenue = current_conversions * avg_order_value
    current_profit = current_revenue * 0.3  # 假设 30% 利润率
    
    # GEO 后
    new_traffic = current_monthly_traffic * geo_boost_factor
    new_conversion_rate = current_conversion_rate + conversion_rate_lift
    new_conversions = new_traffic * new_conversion_rate
    new_revenue = new_conversions * avg_order_value
    new_profit = new_revenue * 0.3
    
    # 增量
    incremental_traffic = new_traffic - current_monthly_traffic
    incremental_revenue = new_revenue - current_revenue
    incremental_profit = new_profit - current_profit
    
    # ROI
    monthly_roi = (incremental_profit / geo_investment_monthly) * 100
    annual_roi = (incremental_profit * 12 / (geo_investment_monthly * 12)) * 100
    payback_months = geo_investment_monthly / incremental_profit if incremental_profit > 0 else float('inf')
    
    return {
        'current': {
            'traffic': current_monthly_traffic,
            'conversions': current_conversions,
            'revenue': current_revenue,
            'profit': current_profit,
        },
        'after_geo': {
            'traffic': new_traffic,
            'conversions': new_conversions,
            'revenue': new_revenue,
            'profit': new_profit,
        },
        'incremental': {
            'traffic': incremental_traffic,
            'revenue': incremental_revenue,
            'profit': incremental_profit,
        },
        'roi': {
            'monthly_pct': monthly_roi,
            'annual_pct': annual_roi,
            'payback_months': payback_months,
        }
    }


def interactive_mode():
    print(f"\n{'='*60}")
    print(f"  💰 GEO ROI 估算器 v1.0")
    print(f"{'='*60}\n")
    
    print("  回答 5 个问题,30 秒算出 GEO 投资回报:\n")
    
    try:
        traffic = int(input("  1. 你现在月访问量(UV): "))
        cr = float(input("  2. 你现在转化率(0.01 = 1%): "))
        aov = float(input("  3. 平均订单价值(元): "))
        investment = int(input("  4. 你愿意每月 GEO 投入(元): "))
        
        print("\n  5. 预估 GEO 提升幅度(选一个):")
        print("     1. 保守(流量+20%,转化率+0.3%)")
        print("     2. 中等(流量+30%,转化率+0.5%)[推荐]")
        print("     3. 乐观(流量+50%,转化率+1%)")
        level = input("  请选(1-3): ")
        
        if level == '1':
            boost, lift = 1.2, 0.003
        elif level == '3':
            boost, lift = 1.5, 0.01
        else:
            boost, lift = 1.3, 0.005
        
    except (ValueError, KeyboardInterrupt):
        print("\n  ❌ 输入无效")
        return
    
    result = calculate_roi(
        current_monthly_traffic=traffic,
        current_conversion_rate=cr,
        avg_order_value=aov,
        geo_investment_monthly=investment,
        geo_boost_factor=boost,
        conversion_rate_lift=lift,
    )
    
    print(f"\n{'='*60}")
    print(f"  📊 估算结果")
    print(f"{'='*60}\n")
    
    print(f"  【当前】")
    print(f"    月访问量:   {result['current']['traffic']:>10,.0f} UV")
    print(f"    月转化:     {result['current']['conversions']:>10,.0f} 单")
    print(f"    月营收:     ¥{result['current']['revenue']:>10,.0f}")
    print(f"    月利润:     ¥{result['current']['profit']:>10,.0f}")
    
    print(f"\n  【GEO 后】")
    print(f"    月访问量:   {result['after_geo']['traffic']:>10,.0f} UV")
    print(f"    月转化:     {result['after_geo']['conversions']:>10,.0f} 单")
    print(f"    月营收:     ¥{result['after_geo']['revenue']:>10,.0f}")
    print(f"    月利润:     ¥{result['after_geo']['profit']:>10,.0f}")
    
    print(f"\n  【增量】")
    print(f"    月访问增量: {result['incremental']['traffic']:>10,.0f} UV")
    print(f"    月利润增量: ¥{result['incremental']['profit']:>10,.0f}")
    
    print(f"\n  【ROI】")
    print(f"    月 ROI:     {result['roi']['monthly_pct']:>10.0f}%")
    print(f"    年 ROI:     {result['roi']['annual_pct']:>10.0f}%")
    print(f"    回本周期:   {result['roi']['payback_months']:.1f} 个月")
    
    # 评估
    monthly_roi = result['roi']['monthly_pct']
    if monthly_roi < 0:
        print(f"\n  ⚠️ GEO 投入超过增量利润,可能不值得")
    elif monthly_roi < 100:
        print(f"\n  ⚡ GEO 有正回报,但回报期较长")
    elif monthly_roi < 500:
        print(f"\n  ✅ GEO 有不错的回报")
    else:
        print(f"\n  🎉 GEO 投入回报极高,值得做!")


def main():
    parser = argparse.ArgumentParser(description='GEO ROI 估算器')
    parser.add_argument('--traffic', type=int, help='当前月访问量')
    parser.add_argument('--cr', type=float, help='当前转化率(如 0.02 = 2%)')
    parser.add_argument('--aov', type=float, help='平均订单价值')
    parser.add_argument('--investment', type=int, help='月 GEO 投入')
    parser.add_argument('--level', choices=['1', '2', '3'], help='预估提升(1=保守,2=中等,3=乐观)')
    
    args = parser.parse_args()
    
    if not args.traffic:
        interactive_mode()
        return
    
    level = args.level or '2'
    if level == '1':
        boost, lift = 1.2, 0.003
    elif level == '3':
        boost, lift = 1.5, 0.01
    else:
        boost, lift = 1.3, 0.005
    
    result = calculate_roi(
        current_monthly_traffic=args.traffic,
        current_conversion_rate=args.cr,
        avg_order_value=args.aov,
        geo_investment_monthly=args.investment,
        geo_boost_factor=boost,
        conversion_rate_lift=lift,
    )
    
    print(f"\n  ROI: {result['roi']['monthly_pct']:.0f}%/月, 回本 {result['roi']['payback_months']:.1f} 月")


if __name__ == "__main__":
    main()
