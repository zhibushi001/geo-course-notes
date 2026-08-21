#!/usr/bin/env python3
"""
Referrer Spam 检测工具 v1.0
分析百度统计导出,自动标记可疑来源

用法:python referrer_spam_checker.py 来源域名列表.txt
"""
import sys
import requests
import re
from urllib.parse import urlparse

def check_baidu_weight(domain):
    """检查百度权重(通过站长之家)"""
    try:
        url = f"https://rank.chinaz.com/{domain}"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)
        # 提取权重数字
        match = re.search(r'百度权重[：:]\s]([\d/]+)', r.text)
        return match.group(1) if match else "未知"
    except:
        return "查询失败"

def check_accessible(domain):
    """检查域名是否可访问"""
    try:
        r = requests.get(f"https://{domain}", timeout=5,
                         headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            return "✅ 可访问"
        elif r.status_code == 403:
            return "🛡️ Cloudflare 拦截"
        elif r.status_code == 404:
            return "❌ 404 不存在"
        else:
            return f"⚠️ {r.status_code}"
    except:
        return "❌ 无法访问"

def check_ahrefs_backlink(domain):
    """通过 Ahrefs 检查外链(需付费)"""
    # 这里是占位,实际需要 Ahrefs API
    return "需 Ahrefs 账号"

def analyze_domain(domain):
    """综合分析"""
    print(f"\n{'='*60}")
    print(f"🔍 分析: {domain}")
    print(f"{'='*60}")
    
    weight = check_baidu_weight(domain)
    access = check_accessible(domain)
    
    print(f"  百度权重: {weight}")
    print(f"  访问状态: {access}")
    
    # 判断
    is_spam = False
    reasons = []
    
    if weight == "0" or weight == "0/0":
        is_spam = True
        reasons.append("百度权重为 0")
    
    if "拦截" in access or "不存在" in access or "无法" in access:
        is_spam = True
        reasons.append(f"访问异常: {access}")
    
    if is_spam:
        print(f"\n  🚨 判定:Referrer Spam")
        print(f"  原因:")
        for r in reasons:
            print(f"    - {r}")
    else:
        print(f"\n  ✅ 判定:可能是真实流量")
    
    return is_spam

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:python referrer_spam_checker.py 域名1.com 域名2.com ...")
        sys.exit(1)
    
    print("\n🔍 Referrer Spam 检测工具 v1.0")
    print("=" * 60)
    
    spam_count = 0
    for domain in sys.argv[1:]:
        if analyze_domain(domain):
            spam_count += 1
    
    print(f"\n{'='*60}")
    print(f"📊 总结: {spam_count}/{len(sys.argv)-1} 个为 Referrer Spam")
    print(f"{'='*60}\n")
