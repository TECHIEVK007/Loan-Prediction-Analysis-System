package com.sahutech.loanpredictionanalysissystem

import android.annotation.SuppressLint
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_main)

        webView = findViewById(R.id.webView)

        // Keep all website links inside the app
        webView.webViewClient = WebViewClient()

        // Enable JavaScript for the website
        webView.settings.javaScriptEnabled = true

        // Enable browser storage
        webView.settings.domStorageEnabled = true

        // Make the website fit properly on mobile
        webView.settings.loadWithOverviewMode = true
        webView.settings.useWideViewPort = true

        // Loan Prediction Flask Website
        webView.loadUrl("http://10.241.192.66:5000")

        // Handle Android back button
        onBackPressedDispatcher.addCallback(
            this,
            object : OnBackPressedCallback(true) {

                override fun handleOnBackPressed() {

                    if (webView.canGoBack()) {
                        webView.goBack()
                    } else {
                        finish()
                    }
                }
            }
        )
    }
}