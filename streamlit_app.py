import streamlit as st
import defang

def defang_text(text_input):
    defanged_text = defang.defang(text_input, all=True)
    return defanged_text

def main():
    st.title("Defang Tool")

    text_input = st.text_area("Enter text to defang:")

    if st.button("Defang"):
        defanged_text = defang_text(text_input)
        st.write("Defanged Text:")
        st.write(defanged_text)

if __name__ == "__main__":
    main()
