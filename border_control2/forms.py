from django import forms


class BorderControl2Form(forms.Form):
    # Task 1 Input Fields (Straight, Reverse, Additional Codes)
    straight_1 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_1 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_1 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_2 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_2 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_2 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_3 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_3 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_3 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_4 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_4 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_4 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    # Task 2 Input Fields (Straight, Reverse, Additional Codes)
    straight_5 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_5 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_5 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_6 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_6 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_6 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_7 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_7 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_7 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_8 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_8 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_8 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_9 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_9 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_9 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    straight_10 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    reversed_10 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    additional_10 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    # Task 3 Input Fields (All Codes for Various Operations)
    temp_11 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_11 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_11 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_11 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_12 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_12 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_12 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_12 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_13 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_13 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_13 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_13 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_14 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_14 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_14 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_14 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_15 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_15 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_15 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_15 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_16 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_16 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_16 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_16 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_17 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_17 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_17 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_17 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )

    temp_18 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "10"}),
    )
    correction_18 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "1"}),
    )
    result_18 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
    realizing_18 = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "max_length": "9"}),
    )
