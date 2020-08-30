using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using MobileApp.Droid;
using MobileApp.Interfaces;
using Xamarin.Forms;

[assembly: Xamarin.Forms.Dependency(typeof(LaunchActivity))]
namespace MobileApp.Droid
{
    public class LaunchActivity : ILaunchActivity
    {
        public LaunchActivity()
        {
        }
        public void LaunchMethod()
        {
            var intent = new Intent(Forms.Context, typeof(SendNfcActivity));
            Forms.Context.StartActivity(intent);
        }

    }
}