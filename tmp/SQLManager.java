import java.sql.*;

public class SQLManager {
    public static void main(String[] args) {
        String jdbcUrl = "jdbc:mysql://localhost:3306/stockdb";
        String user = "root";
        String password = "";

        try {
            // MySQL 드라이버 로드
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // 데이터베이스 연결
            Connection connection = DriverManager.getConnection(jdbcUrl, user, password);
            
            if (connection != null) {
                System.out.println("MySQL 데이터베이스에 성공적으로 연결되었습니다.");
                
                // 여기에 원하는 작업을 수행합니다.
                
                // 연결 종료
                connection.close();
            }
        } catch (ClassNotFoundException e) {
            System.out.println("드라이버 클래스를 찾을 수 없습니다.");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println("MySQL 데이터베이스 연결 중 오류가 발생했습니다.");
            e.printStackTrace();
        }
    }
}