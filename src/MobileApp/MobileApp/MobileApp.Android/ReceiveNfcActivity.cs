using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.Nfc;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace MobileApp.Droid
{
    [Activity, IntentFilter(new[] { "android.nfc.action.NDEF_DISCOVERED" },
        Categories = new[] { "android.intent.category.DEFAULT" })]
    public class ReceiveNfcActivity : Activity
    {
        private TextView _textView;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.DisplayNfc);
            if (Intent == null)
            {
                return;
            }

            var intentType = Intent.Type ?? String.Empty;
      
            _textView = FindViewById<TextView>(Resource.Id.read_nfc_text_view);

            var button = FindViewById<Button>(Resource.Id.back_to_main_activity);
            button.Click += (sender, args) => Finish();

            var rawMessages = Intent.GetParcelableArrayExtra(NfcAdapter.ExtraNdefMessages);
            var msg = (NdefMessage)rawMessages[0];
            var record = msg.GetRecords()[0];
            var message = Encoding.ASCII.GetString(record.GetPayload());
            DisplayMessage(message);

        }

        private void DisplayMessage(string message)
        {
            _textView.Text = message;
            //Log.Info(Tag, message);
        }

    }
}
