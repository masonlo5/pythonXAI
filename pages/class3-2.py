import streamlit as st

st.title("food service machine")
if "order" not in st.session_state:
    st.session_state.order = []

ss_order = st.session_state.order 

col1, col2 = st.columns(2)
with col1:
    # 左側欄位：輸入欲點的菜名
    dishes = st.text_input("write dishes name")

# 右側欄位：放置新增按鈕（與左側同層，而非巢狀於左側）
with col2:
    # 按下 add 時將輸入的菜名加入 session_state 的 order（購物車）
    if st.button("add", key="add_order"):
        ss_order.append(dishes)

st.title("cart")

for i in range(len(ss_order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(ss_order[i])
    with col2:
        # 刪除按鈕：使用明確 key（避免與其他按鈕 key 衝突）
        if st.button("delete", key=f"del_{i}"):
            ss_order.pop(i)  # 從購物車中移除該項目
            st.rerun()  # 重新執行頁面以更新顯示