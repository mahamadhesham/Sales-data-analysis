import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "date": [
        "2026-01-05", "2026-01-08", "2026-01-12", "2026-01-15",
        "2026-02-02", "2026-02-10", "2026-02-18", "2026-02-25",
        "2026-03-03", "2026-03-07", "2026-03-15", "2026-03-22"
    ],
    "product": [
        "Laptop", "Phone", "Laptop", "Tablet",
        "Phone", "Laptop", "Tablet", "Phone",
        "Laptop", "Tablet", "Phone", "Laptop"
    ],
    "category": [
        "Electronics", "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics", "Electronics"
    ],
    "region": [
        "Cairo", "Giza", "Cairo", "Alexandria",
        "Giza", "Cairo", "Alexandria", "Cairo",
        "Giza", "Alexandria", "Cairo", "Giza"
    ],
    "quantity": [2, 5, 1, 3, 4, 2, 5, 6, 3, 4, 7, 2],
    "price": [30000, 18000, 30000, 12000, 18000, 30000,
              12000, 18000, 30000, 12000, 18000, 30000]
})
df["revenue"]=df["quantity"]*df["price"]
df["date"]=pd.to_datetime(df["date"])
df["year"]=df["date"].dt.year
df["month"]=df["date"].dt.month
df["month_name"]=df["date"].dt.month_name()
df["day"]=df["date"].dt.date
df["day_name"]=df["date"].dt.day_name()
product_rev=df.groupby("product")["revenue"].sum()
region_revenue=df.groupby("region")["revenue"].sum()
average_selling_price=df.groupby("product")["price"].mean()
region_sold_highest_total_quantity_products=df.groupby("region")["quantity"].sum()
product_generated_highest_rev_in_each_region=df.groupby(["region","product"])["revenue"].sum()
result1=product_generated_highest_rev_in_each_region.groupby(level=0).idxmax()
month_generated_highest_total_rev=df.groupby("month")["revenue"].sum()
product_quantity=df.groupby("product")["quantity"].sum()
highest_quantity_product=product_quantity.idxmax()
highest_quantity=product_quantity.max()
average_region_table=df.groupby("region")["revenue"].mean()
highest_average_region_as_number=average_region_table.max()
highest_average_region_name=average_region_table.idxmax()
region_product_quantity=df.groupby(["region","product"])["quantity"].sum()
result2=region_product_quantity.groupby(level=0).idxmax()
product_revenue=df.groupby("product")["revenue"].sum()
product_percentage=product_revenue/product_revenue.sum() *100
product_month_revenue=df.groupby(["month_name","product"])["revenue"].sum()
result3=product_month_revenue.groupby(level=0).idxmax()
region_month_revenue=df.groupby(["month_name","region","product"])["revenue"].sum()
result4=region_month_revenue.groupby(level=0).idxmax()
result5=region_product_quantity.sort_values(ascending=False)
revenue_of_week_day=df.groupby("day_name")["revenue"].sum()
highest_week_day_revenue=revenue_of_week_day.idxmax()
correlation=df[["quantity","revenue"]].corr()
plt.figure(figsize=(8, 5))
plt.scatter(df["quantity"], df["revenue"])
plt.xlabel("Quantity")
plt.ylabel("Revenue (EGP)")
plt.title("Quantity vs Revenue")
plt.tight_layout()
plt.savefig("quantity_vs_revenue.png", dpi=300, bbox_inches="tight")

correlation2=df[["price","revenue"]].corr()
region_analysis=df.groupby("region").agg({
    "revenue":"sum",
    "quantity":"sum",
    "price":"mean"
    })
average_revenue_for_each_product_in_region=pd.pivot_table(
    df,
    values="revenue",
    index="region",
    columns="product",
    aggfunc="mean"
)
average_revenue_for_each_product_in_region.idxmax(axis=1)
each_product_highest_region_total_revenue=pd.pivot_table(
    df,
    values="revenue",
    index="product",
    columns="region",
    aggfunc="sum"
)
#idxmax(axis=1) means biggest in every row 
highest_total_rev_for_each_month=df.groupby(["month_name","region"])["revenue"].sum()
result6=highest_total_rev_for_each_month.groupby(level=0).idxmax()
region_contribution_percentage=region_revenue/region_revenue.sum() *100
highest_total_rev_for_each_month_name=df.groupby(["product","month_name"])["revenue"].sum()
result7=highest_total_rev_for_each_month_name.groupby(level=0).idxmax()
average_quantity_for_each_product_in_each_region=pd.pivot_table(
    df,
    values="quantity",
    index="region",
    columns="product",
    aggfunc="mean"
)
each_region_highest_total_quantity_product=pd.pivot_table(
    df,
    values="quantity",
    index="region",
    columns="product",
    aggfunc="sum"
)
result8=each_region_highest_total_quantity_product.idxmax(axis=1)
result9=average_selling_price.idxmax()
result10=average_selling_price.max()
Revenue_sum_for_every_month_name=df.groupby("month_name")["revenue"].sum()
result11=Revenue_sum_for_every_month_name.sort_values(ascending=False)
Revenue_sum_for_every_month=df.groupby("month")["revenue"].sum()
result12=Revenue_sum_for_every_month.diff()  #Diff means the current value-Past value
growth_percentage=(result12/Revenue_sum_for_every_month.shift(1))*100
A_month_with_highest_revenue_growth_percentage=growth_percentage.idxmax()
product_generated_highest_rev_growth_from_Jan_to_March=df.groupby(["product","month"])["revenue"].sum()
result13=product_generated_highest_rev_growth_from_Jan_to_March.unstack()
result14=(result13[3]-result13[1])/result13[1] *100
Region_with_highest_rev_from_Jan_to_mar=df.groupby(["region","month"])["revenue"].sum()
result15=Region_with_highest_rev_from_Jan_to_mar.unstack()
result16=(result15[3]-result15[1])/result15[1]*100
Each_region_the_product_highest_revenue_from_Jan_to_mar=df.groupby(["region","product","month"])["revenue"].sum()
result17=Each_region_the_product_highest_revenue_from_Jan_to_mar.unstack()
result18=(result17[3]-result17[1])/result17[1] *100
average_quantity_per_product=df.groupby("product")["quantity"].mean()
result19=average_quantity_per_product.idxmax()
region_average_quantity=df.groupby("region")["quantity"].mean()
result20=region_average_quantity.idxmax()
product_with_average_revenue=df.groupby("product")["revenue"].mean()
result21=product_with_average_revenue.idxmax()
region_with_average_revenue=df.groupby("region")["revenue"].mean()
result22=region_with_average_revenue.idxmax()
A_month_average_revenue=df.groupby("month")["revenue"].mean()
result23=A_month_average_revenue.idxmax()
month_average_quantity=df.groupby("month")["quantity"].mean()
result24=month_average_quantity.idxmax()
revenue_per_unit=product_revenue/product_quantity
result25=revenue_per_unit.idxmax()
region_total_rev=region_revenue/df.groupby("region")["quantity"].sum()
result26=region_total_rev.idxmax()
highest_product_revenue_each_month=pd.pivot_table(
    df,
    values="revenue",
    index="month",
    columns="product",
    aggfunc="sum"
)
result27=highest_product_revenue_each_month.idxmax(axis=1)
highest_region_revenue_each_month=pd.pivot_table(
    df,
    values="revenue",
    index="month",
    columns="region",
    aggfunc="sum"
)
result28=highest_region_revenue_each_month.idxmax(axis=1)
total_region_product_quantity=pd.pivot_table(
    df,
    values="quantity",
    index="region",
    columns="product",
    aggfunc="sum"
)
result29=total_region_product_quantity.idxmax(axis=1)
result30=average_selling_price.idxmax()
highest_product_revenue_each_region=pd.pivot_table(
    df,
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum"
)
result31=highest_product_revenue_each_region
highest_region_revenue_each_product=pd.pivot_table(
    df,
    values="revenue",
    index="product",
    columns="region",
    aggfunc="sum"
)
result32=highest_region_revenue_each_product.idxmax(axis=1)
region_highest_rev_for_each_product=pd.pivot_table(
    df,
    values="revenue",
    index="product",
    columns="region",
    aggfunc="sum"
)
result33=region_highest_rev_for_each_product.idxmax(axis=1)
region_highest_rev_growth_from_jan_mars=df.groupby(["region","month"])["revenue"].sum()
result34=region_highest_rev_growth_from_jan_mars.unstack()
result35=(result34[3]-result34[1])/result34[1]*100
average_selling_price_by_region=df.groupby("region")["price"].mean()
result36=average_selling_price_by_region.idxmax()
result37=region_average_quantity.idxmax()
result38=product_with_average_revenue.idxmax()
result39=region_with_average_revenue.idxmax()
result40=A_month_average_revenue.idxmax()
result41=month_average_quantity.idxmax()
result42=average_quantity_per_product.idxmax()
result43=product_quantity.idxmax()
result44=average_quantity_per_product.idxmax()
result45=product_percentage.idxmax()
result46=region_contribution_percentage.idxmax()
result47=region_with_average_revenue.idxmax()
monthly_revenue=df.groupby("month")["revenue"].sum()
monthly_revenue_percentage=(monthly_revenue/monthly_revenue.sum())*100
result48=monthly_revenue_percentage.idxmax()
month_total_quantity=df.groupby("month")["quantity"].sum()
result49=month_total_quantity.idxmax()
total_revenue_of_months=df.groupby("month")["revenue"].sum()
result50=total_revenue_of_months.idxmin()
result51=product_revenue.idxmin()
result52=region_revenue.idxmin()
result53=average_selling_price.idxmin()
result54=average_quantity_per_product.idxmin()
result55=region_average_quantity.idxmin()
result56=revenue_per_unit.idxmax()
result57=region_total_rev.idxmax()
result58=A_month_average_revenue.idxmin()
average_revenue_per_sale=df.groupby("product")["revenue"].mean()
result59=average_revenue_per_sale.idxmin()
result60=region_with_average_revenue.idxmin()
result61=month_average_quantity.idxmin()
result62=revenue_per_unit.idxmin()
result63=region_total_rev.idxmin()
month_rev_per_unit_sold=A_month_average_revenue/month_average_quantity
result64=month_rev_per_unit_sold.idxmin()
product_total_quantity_percentage=(product_quantity/product_quantity.sum())*100
result65=product_total_quantity_percentage.idxmax()
region_total_quantity_percentage=(region_sold_highest_total_quantity_products/region_sold_highest_total_quantity_products.sum())*100
result66=region_total_quantity_percentage.idxmax()
month_total_quantity_percentage=(month_total_quantity/month_total_quantity.sum())*100
result67=month_total_quantity_percentage.idxmax()
result68=month_total_quantity_percentage.idxmin()
product_revenue_each_region_percentage=(highest_product_revenue_each_region/highest_product_revenue_each_region.sum())*100
result69=product_revenue_each_region_percentage.idxmax(axis=1)
result70=product_revenue_each_region_percentage.idxmin(axis=1)
result71=region_contribution_percentage.idxmax()
result72=region_contribution_percentage.idxmin()
result73=product_percentage.idxmax()
result74=product_percentage.idxmin()
result75=monthly_revenue_percentage.idxmax()
result76=monthly_revenue_percentage.idxmin()
result77=product_total_quantity_percentage.idxmax()
result78=region_total_quantity_percentage.idxmax()
result79=month_total_quantity_percentage.idxmax()
result80=month_total_quantity_percentage.idxmin()
result81=product_revenue_each_region_percentage.idxmax(axis=1)
result82=product_revenue_each_region_percentage.idxmin(axis=1)
total_region_product_quantity_percentage=(total_region_product_quantity/total_region_product_quantity.sum(axis=1).values[:,None])*100
result83=total_region_product_quantity_percentage.idxmax(axis=1)
reason_of_generating_more_in_march=df.groupby("month")["quantity"].sum()
product_revenue_growth_feb_mar=((product_month_revenue["March"]-product_month_revenue["February"])/product_month_revenue["February"])*100
highest_product_revenue_growth=product_revenue_growth_feb_mar.idxmax()
region_revenue_growth_feb_mar=((region_month_revenue["March"]-region_month_revenue["February"])/region_month_revenue["February"])*100
highest_region_revenue_growth=region_revenue_growth_feb_mar.idxmax()
region_product_revenue_feb_mar=df.groupby(["region","product","month"])["revenue"].sum()
region_product_revenue_feb_mar=region_product_revenue_feb_mar.unstack(fill_value=0)
revenue_growth_feb_mar=(region_product_revenue_feb_mar[3]-region_product_revenue_feb_mar[2])
highest_revenue_increase=revenue_growth_feb_mar.idxmax()
region_month_quantity_feb_mar=df.groupby(["region","month"])["quantity"].sum()
region_month_quantity_feb_mar=region_month_quantity_feb_mar.unstack(fill_value=0)
giza_quantity_growth=(
    (region_month_quantity_feb_mar.loc["Giza",3] 
     -
       region_month_quantity_feb_mar.loc["Giza",2])
       /region_month_quantity_feb_mar.loc["Giza",2]*100)
region_revenue_febr_march=df.groupby(["region","month"])["revenue"].sum()
region_month_quantity_febr_march=df.groupby(["region","month"])["quantity"].sum()
region_revenue_febr_march=region_revenue_febr_march.unstack(fill_value=0)
region_month_quantity_febr_march=region_month_quantity_febr_march.unstack(fill_value=0)
region_revenue_growth=((region_revenue_febr_march[3]-region_revenue_febr_march[2])/region_revenue_febr_march[2]*100)
region_quantity_growth=((region_month_quantity_febr_march[3]-region_month_quantity_febr_march[2])/region_month_quantity_febr_march[2])*100
business_insights=[
    "Phones generated 47.14% of total revenue.",
    "Laptops generated the highest revenue per unit at EGP 30,000.",
    "Cairo generated the highest total revenue at EGP 360,000",
    "Giza generated the highest revenue per unit at EGP 24,000",
    "Profitability cannot be determined without cost data."
]
for insight in business_insights:
    print("-", insight)
plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar")
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (EGP)")
plt.xticks(rotation=0)
for container in plt.gca().containers:
    plt.bar_label(container, fmt="%.0f")

plt.tight_layout()
plt.savefig("revenue_by_product.png", dpi=300, bbox_inches="tight")


# 2. Monthly revenue
plt.figure(figsize=(8, 5))
monthly_revenue.plot(kind="bar")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (EGP)")
plt.xticks(
    ticks=range(len(monthly_revenue)),
    labels=["January", "February", "March"],
    rotation=0
)

for container in plt.gca().containers:
    plt.bar_label(container, fmt="%.0f")

plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=300, bbox_inches="tight")


# Display all charts
plt.show()

product_sales_comparison=pd.DataFrame({
    "Total Quantity":product_quantity,
    "Total Revenue":product_revenue
})
product_sales_comparison
highest_revenue_per_unit=revenue_per_unit.idxmax()
highest_value=revenue_per_unit.max()
print(f"{highest_revenue_per_unit} has the highest revenue per unit: "
      f"EGP {highest_value:,.0f}"
)
feb_to_mar_revenue_growth=(
    (monthly_revenue[3]-monthly_revenue[2])/monthly_revenue[2]
)*100
print(
    f"Revenue growth from February to March: "
    f"{feb_to_mar_revenue_growth:.2f}%"
)
plt.show()