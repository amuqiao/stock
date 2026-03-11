#!/usr/bin/env python3
import json
import sys
import os

def extract_codes(file_path):
    """从JSON文件中提取股票代码并返回逗号分隔的字符串"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        codes = [item['code'] for item in data if 'code' in item]
        return ','.join(codes)
    except Exception as e:
        print(f"读取文件出错: {e}")
        return ""

def main():
    """主函数"""
    # 默认文件路径
    watchlist_path = "/Users/wangqiao/Downloads/github_project/stock/stock_investment/watchlist.json"
    holdings_path = "/Users/wangqiao/Downloads/github_project/stock/stock_investment/holdings.json"
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        # 如果用户提供了文件路径
        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            sys.exit(1)
    else:
        # 提示用户选择文件
        print("请选择要读取的文件:")
        print("1. watchlist.json")
        print("2. holdings.json")
        
        choice = input("请输入您的选择 (1 或 2): ")
        if choice == '1':
            file_path = watchlist_path
        elif choice == '2':
            file_path = holdings_path
        else:
            print("无效选择，默认使用 watchlist.json")
            file_path = watchlist_path
    
    # 提取并打印代码
    codes = extract_codes(file_path)
    print(f"来自 {os.path.basename(file_path)} 的股票代码:")
    print(codes)

if __name__ == "__main__":
    main()
