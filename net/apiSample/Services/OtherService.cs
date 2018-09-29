
public interface IOtherService
{
    string GetMessage();
}

public class OtherService : IOtherService {

    public string GetMessage() 
    {
        return "Hi Josh!";
    }
}