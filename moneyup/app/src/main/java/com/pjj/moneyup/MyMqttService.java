


package com.pjj.moneyup;

import android.annotation.SuppressLint;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Binder;
import android.os.Build;
import android.os.IBinder;
//import android.support.annotation.Nullable;
import android.util.Log;

import androidx.annotation.RequiresApi;
import androidx.core.app.NotificationCompat;


import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.Arrays;
import java.util.Random;

/**
 * Author       wildma
 * Github       https://github.com/wildma
 * CreateDate   2018/11/08
 * Desc	        ${MQTT服务}
 */

public class MyMqttService extends Service {

    public final String TAG = MyMqttService.class.getSimpleName();
    private static MqttAndroidClient mqttAndroidClient;
    private MqttConnectOptions mMqttConnectOptions;
    public String HOST = "tcp://129.211.0.201:8889";//服务器地址（协议+地址+端口号）
    public String USERNAME = "mymoneyup";//用户名
    public String PASSWORD = "1U3rS6Oo8aKU50o";//密码
    public static String PUBLISH_TOPIC = "moneyup_to";//发布主题
    public static String RESPONSE_TOPIC = "moneyup_re";//响应主题
    @SuppressLint("MissingPermission")
    public String CLIENTID = "mymoneyandroid_01";//客户端ID，一般以客户端唯一标识符表示，这里用设备序列号表示
    public String reMessage = "";

    public NotificationManager notificationManager;
    public Notification notification = null;
    public String ChanelId = "12";
//    private Bitmap LargeBitmap;
    public JSONObject obj;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        return super.onStartCommand(intent, flags, startId);
    }

    //定义onBinder方法所返回的对象
    private MyBinder binder = new MyBinder();

    public class MyBinder extends Binder {
        public String getMessage() {
            return reMessage;
        }

        public void setMessageNull() {
            reMessage = "";
        }
    }

    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    public void onCreate() {
        super.onCreate();
        Log.i(TAG, "onStartCommand方法被调用!");
        Log.i(TAG, "22222222");
        String name = "name";
        notificationManager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        NotificationChannel mChannel = new NotificationChannel(ChanelId, name, NotificationManager.IMPORTANCE_LOW);
        assert notificationManager != null;
        notificationManager.createNotificationChannel(mChannel);

        init();
        Log.i(TAG, "33333");
    }

    @RequiresApi(api = Build.VERSION_CODES.O)
    private void notifyMessage() throws JSONException {
        Intent mainIntent = new Intent(this, MainActivity.class);
        PendingIntent mainPendingIntent = PendingIntent.getActivity(this, 0, mainIntent, PendingIntent.FLAG_UPDATE_CURRENT);

        String text = obj.getString("message");//通过name字段获取其所包含的字符串
        String title = obj.getString("title");//通过name字段获取其所包含的字符串
//        LargeBitmap = BitmapFactory.decodeResource(getResources(), R.mipmap.logo);
//        notification = new Notification.Builder(this)
//                .setChannelId(ChanelId)
//                .setContentTitle(title)
//                .setContentText(text)
//                .setContentIntent(mainPendingIntent)
//                .setNumber(5)
//                .setWhen(System.currentTimeMillis())
//                .setPriority(Notification.PRIORITY_DEFAULT)
//                .setAutoCancel(true)
//                .setSmallIcon(R.mipmap.logo).build();

        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "subscribe")
                .setChannelId(ChanelId)
                .setContentTitle(title)
                .setContentText(text)
                .setContentIntent(mainPendingIntent)
                .setNumber(5)
                .setWhen(System.currentTimeMillis())
                .setPriority(Notification.PRIORITY_DEFAULT)
                .setAutoCancel(true)
                .setSmallIcon(R.mipmap.notifi);

        //创建大文本样式
        NotificationCompat.BigTextStyle bigTextStyle = new NotificationCompat.BigTextStyle();
        bigTextStyle.setBigContentTitle(title)
//                .setSummaryText("哈哈哈哈哈")
                .bigText(text);

        builder.setStyle(bigTextStyle); //设置大文本样式
        notification = builder.build();


        notificationManager.notify((int) (1 + Math.random() * 100), notification);//把通知显示出来
//        startForeground(1,notification);//前台通知(会一直显示在通知栏)
    }

    @Override
    public IBinder onBind(Intent intent) {

        return binder;
    }

    /**
     * 发布 （模拟其他客户端发布消息）
     *
     * @param message 消息
     */
    public static void publish(String message) {
        String topic = PUBLISH_TOPIC;
        int qos = 2;
        boolean retained = false;
        try {
            //参数分别为：主题、消息的字节数组、服务质量、是否在服务器保留断开连接后的最后一条消息
            mqttAndroidClient.publish(topic, message.getBytes(), (int) qos, retained);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    /**
     * 响应 （收到其他客户端的消息后，响应给对方告知消息已到达或者消息有问题等）
     *
     * @param message 消息
     */
    public void response(String message) {
        String topic = RESPONSE_TOPIC;
        int qos = 2;
        boolean retained = false;
        try {
            //参数分别为：主题、消息的字节数组、服务质量、是否在服务器保留断开连接后的最后一条消息
            mqttAndroidClient.publish(topic, message.getBytes(), (int) qos, retained);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }

    /**
     * 初始化
     */
    private void init() {
        String serverURI = HOST; //服务器地址（协议+地址+端口号）
        mqttAndroidClient = new MqttAndroidClient(this, serverURI, CLIENTID);
        mqttAndroidClient.setCallback(mqttCallback); //设置监听订阅消息的回调
        mMqttConnectOptions = new MqttConnectOptions();
//        mMqttConnectOptions.setCleanSession(true); //设置是否清除缓存
        mMqttConnectOptions.setConnectionTimeout(10); //设置超时时间，单位：秒
        mMqttConnectOptions.setKeepAliveInterval(10); //设置心跳包发送间隔，单位：秒
        mMqttConnectOptions.setUserName(USERNAME); //设置用户名
        mMqttConnectOptions.setPassword(PASSWORD.toCharArray()); //设置密码

        // last will message
        boolean doConnect = true;
        String message = "{\"terminal_uid\":\"" + CLIENTID + "\"}";
        String topic = PUBLISH_TOPIC;
        int qos = 2;
        boolean retained = false;
        if ((!message.equals("")) || (!topic.equals(""))) {
            // 最后的遗嘱
            try {
                mMqttConnectOptions.setWill(topic, message.getBytes(), (int) qos, retained);
            } catch (Exception e) {
                Log.i(TAG, "Exception Occured", e);
                doConnect = false;
                iMqttActionListener.onFailure(null, e);
            }
        }
        if (doConnect) {
            doClientConnection();
        }
    }

    /**
     * 连接MQTT服务器
     */
    private void doClientConnection() {
        if (!mqttAndroidClient.isConnected()) {
            try {
                mqttAndroidClient.connect(mMqttConnectOptions, null, iMqttActionListener);
            } catch (MqttException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * 判断网络是否连接
     */
//    private boolean isConnectIsNomarl() {
//        ConnectivityManager connectivityManager = (ConnectivityManager) this.getApplicationContext().getSystemService(Context.CONNECTIVITY_SERVICE);
//        NetworkInfo info = connectivityManager.getActiveNetworkInfo();
//        if (info != null && info.isAvailable()) {
//            String name = info.getTypeName();
//            Log.i(TAG, "当前网络名称：" + name);
//            return true;
//        } else {
//            Log.i(TAG, "没有可用网络");
//            /*没有可用网络的时候，延迟3秒再尝试重连*/
//            new Handler().postDelayed(new Runnable() {
//                @Override
//                public void run() {
//                    doClientConnection();
//                }
//            }, 3000);
//            return false;
//        }
//    }

    //MQTT是否连接成功的监听
    private IMqttActionListener iMqttActionListener = new IMqttActionListener() {

        @Override
        public void onSuccess(IMqttToken arg0) {
            Log.i(TAG, "连接成功 ");
            try {
                mqttAndroidClient.subscribe(PUBLISH_TOPIC, 2);//订阅主题，参数：主题、服务质量
            } catch (MqttException e) {
                e.printStackTrace();
            }
        }

        @Override
        public void onFailure(IMqttToken arg0, Throwable arg1) {
            arg1.printStackTrace();
            Log.i(TAG, "连接失败 ");
            doClientConnection();//连接失败，重连（可关闭服务器进行模拟）
        }
    };

    //订阅主题的回调
    private MqttCallback mqttCallback = new MqttCallback() {

        @RequiresApi(api = Build.VERSION_CODES.O)
        @Override
        public void messageArrived(String topic, MqttMessage message) throws Exception {
            reMessage = new String(message.getPayload());
            Log.i(TAG, "收到消息： " + reMessage);
//            Gson gson = new Gson();
//            jsonArray = gson.toJson(strings, String[].class);

//            String reMessage = "{\"msg_id\": \"191128175542989\", \"message\": \"工商银行 最新价格 5.84 ，比初始价格 5.507  上涨了 6.05 %\", \"updown\": \"up\", \"type\": \"price_change\"}";
//            JSONObject obj = null;
            obj = new JSONObject(reMessage);
            try {
//              JSONObject user = obj.getJSONObject("user");//通过user字段获取其所包含的JSONObject对象
                String msg_id = obj.getString("msg_id");//通过name字段获取其所包含的字符串
//              System.out.println(name);
                String response_msg = "{\"msg_id\":\"" + msg_id + "\"}";
                response(response_msg);
            } catch (JSONException e) {
                e.printStackTrace();
            }

            notifyMessage();
            //收到消息，这里弹出Toast表示。如果需要更新UI，可以使用广播或者EventBus进行发送
//            Toast.makeText(getApplicationContext(), "messageArrived: " + new String(message.getPayload()), Toast.LENGTH_LONG).show();
            //收到其他客户端的消息后，响应给对方告知消息已到达或者消息有问题等
        }

        @Override
        public void deliveryComplete(IMqttDeliveryToken arg0) {

        }

        @Override
        public void connectionLost(Throwable arg0) {
            Log.i(TAG, "连接断开 ");
            doClientConnection();//连接断开，重连
        }
    };

    @Override
    public void onDestroy() {
        try {
            mqttAndroidClient.disconnect(); //断开连接
        } catch (MqttException e) {
            e.printStackTrace();
        }
        super.onDestroy();
    }
}
