package loader;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.net.ServerSocket;
import java.net.Socket;

import java.util.HashMap;


class Server extends Thread {

    private static final HashMap<Integer, string> table_name = new HashMap<Integer, string>();
    private int port;

    public Server(int port) {
        this.port = port;
    }

    public void run() {                                                        // dev와 통신할 포트
        Thread.currentThread().setUncaughtExceptionHandler((thread, throwable) -> {
            System.err.println("스레드에서 예외가 발생하였습니다: " + throwable);
            restartThread();
        });

        try(ServerSocket serverSocket = new ServerSocket(port)) {

            System.out.println("Server waiting at " + port + "...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("client connected");
                
                // message from client
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String string = bufferedReader.readLine();

                System.out.println("서버가 수신한 메세지: " + string);  
                clientSocket.close();      
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void restartThread() {
        // 스레드를 다시 시작하는 로직을 여기에 구현합니다.
        // 예를 들어, 새로운 스레드를 생성하고 start() 메서드를 호출하여 스레드를 다시 시작할 수 있습니다.
        Server newServerThread = new Server(port);
        newServerThread.start();
    }
}