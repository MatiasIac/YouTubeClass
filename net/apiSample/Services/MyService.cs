namespace apiSample {
    public class MyService 
    {
        public string Message 
        { 
            get 
            {
                return _otherService.GetMessage();
            } 
        }

        private readonly OtherService _otherService;

        public MyService(OtherService otherService) {
            _otherService = otherService;
        }
    }
}