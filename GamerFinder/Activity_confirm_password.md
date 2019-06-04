# activity_confirm_password
```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/background"
    tools:context=".Confirm_passwordActivity">

    <ImageView
        android:id="@+id/imgView_logo"
        android:layout_width="259dp"
        android:layout_height="167dp"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="-20dp"
        android:adjustViewBounds="true"
        android:contentDescription="@string/img_logo"
        android:scaleType="fitCenter"
        app:srcCompat="@drawable/logo" />


    <RelativeLayout
        android:id="@+id/rellay1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/imgView_logo">

        <TextView
            android:id="@+id/tv_details"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_alignParentTop="true"
            android:layout_marginTop="1dp"
            android:layout_marginBottom="3dp"
            android:fontFamily="@font/fightingspirit"
            android:gravity="center"
            android:paddingBottom="20dp"
            android:scaleType="fitCenter"
            android:text="@string/app_name"
            android:textColor="#DBE2EF"
            android:textSize="30sp" />

        <LinearLayout
            android:id="@+id/linlay1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_below="@id/tv_details"
            >

            <ImageView
                android:layout_width="40dp"
                android:layout_height="match_parent"
                android:src="@drawable/lock"
                android:layout_marginStart="8dp"
                android:contentDescription="@string/img_lock" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical">

                <android.support.design.widget.TextInputLayout
                    android:layout_height="match_parent"
                    android:layout_width="match_parent"
                    android:paddingBottom="10dp"
                    >
                    <android.support.design.widget.TextInputLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:focusable="true"
                        android:focusableInTouchMode="true"
                        >
                        <EditText
                            android:layout_width="match_parent"
                            android:layout_height="40dp"
                            android:layout_marginTop="5dp"
                            android:background="@drawable/et_bg"
                            android:fontFamily="sans-serif-light"
                            android:textColor="#DBE2EF"
                            android:textSize="20sp"
                            android:hint="@string/et_new_password"
                            android:ems="10"
                            android:paddingLeft="15dp"
                            android:paddingRight="15dp"
                            android:layout_marginLeft="15dp"
                            android:layout_marginRight="15dp"
                            android:inputType="text" />
                    </android.support.design.widget.TextInputLayout>

                </android.support.design.widget.TextInputLayout>



            </LinearLayout>

        </LinearLayout>

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_below="@id/tv_details"
            android:layout_marginTop="55dp"
            android:id="@+id/linlay2"
            >

            <ImageView
                android:layout_width="40dp"
                android:layout_height="match_parent"
                android:src="@drawable/lock"
                android:layout_marginStart="8dp"
                android:contentDescription="@string/img_lock" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical">

                <android.support.design.widget.TextInputLayout
                    android:layout_height="match_parent"
                    android:layout_width="match_parent"
                    android:paddingBottom="10dp">
                    <android.support.design.widget.TextInputLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:focusable="true"
                        android:focusableInTouchMode="true"
                        app:passwordToggleEnabled="true">

                        <EditText
                            android:layout_width="match_parent"
                            android:layout_height="40dp"
                            android:background="@drawable/et_bg"
                            android:fontFamily="sans-serif-light"
                            android:textColor="#DBE2EF"
                            android:textSize="20sp"
                            android:hint="@string/et_confirm_password"
                            android:ems="10"
                            android:paddingLeft="15dp"
                            android:paddingRight="15dp"
                            android:layout_marginLeft="15dp"
                            android:layout_marginRight="15dp"
                            />

                    </android.support.design.widget.TextInputLayout>

                </android.support.design.widget.TextInputLayout>
            </LinearLayout>

        </LinearLayout>



        <Button
            android:id="@+id/btn_Login"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_centerHorizontal="true"
            android:layout_below="@+id/rd_box_remember"
            android:text="@string/btn_Send"
            android:textAllCaps="false"
            android:background="@drawable/btn_bg"
            android:fontFamily="sans-serif-medium"
            android:textColor="#DBE2EF"
            android:layout_marginTop="220dp"
            android:paddingLeft="70dp"
            android:paddingRight="70dp"
            android:textSize="16sp" />
    </RelativeLayout>


</RelativeLayout>
```