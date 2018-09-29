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

        private readonly IOtherService _otherService;

        public MyService(IOtherService otherService) {
            _otherService = otherService;
        }
    }
}