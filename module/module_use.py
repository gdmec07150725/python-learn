import sys

# import fibo
from fibo import fib as fibonacci, fib2

# fibo.fib(1000)
# fibo.fib2(1000)

fibonacci(1000)
fib2(1000)
# 输出模块的名称
# print(fibo.__name__)


def add_product(product, products=[]):
    products.append(product)
    return products


print(add_product("键盘"))
print(add_product("鼠标"))
print(add_product("耳机", []))


def get_paid_orders(orders, user_id):
    # 在这里实现
    result = []
    for order in orders:
        if order["user_id"] == user_id and order["status"] == "paid":
            result.append(order)
    return result


def summarize_orders(orders):
    result = {}
    for order in orders:
        status = order["status"]
        if order.status in result:
            result[status]["count"] += 1
            result[status]["total_amount"] += order['amount']
        else:
            result[status] = {"count": 1, "total_amount": order['amount']}
    return result

def top_paid_orders(orders, *, limit=3):
    result = []
    if limit <= 0:
        return []

    for order in orders:
        if order["status"] == "paid":
            result.append(order)
    # 按金额从大到小排序，金额相同的时候，按订单号从小到大排序  
    sorted_orders = sorted(
        result,
        key = lambda order: (-order["amount"], order["id"])
    )

    return sorted_orders[:limit]

def main():
    # 1. 查询 U01 的已付款订单
    user_orders = get_paid_orders(orders, "U01")
    user_order_ids = [order["id"] for order in user_orders]

    print("U01 的已付款订单：", user_order_ids)

    # 2. 按状态统计
    summary = summarize_orders(orders)

    print("各状态统计：")

    # summary对象的遍历, status是key，statistics 是对象一整个值
    for status, statistics in summary.items():
        print(
            status,
            "数量：", statistics["count"],
            "金额合计：", statistics["total_amount"],
            "分",
        )

    # 3. 获取金额最高的三笔已付款订单
    top_orders = top_paid_orders(orders, limit=3)
    top_order_ids = [order["id"] for order in top_orders]

    print("金额最高的三笔已付款订单：", top_order_ids)

    # 4. 获取去重后的用户编号
    user_ids = get_user_ids(orders)

    print("用户编号：", user_ids)


if __name__ == "__main__":
    main()