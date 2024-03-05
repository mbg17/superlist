s = "a,b"
d = [{'key': 'a'}, {'key': 'b'}, {'key': 'c'}]

for i in d:
    if list(i.values())[0] in [x for x in s.split(",")]:
        i['flag'] = '1'
    else:
        i['flag'] = '0'
print(d)

System.setProperty("webdriver.chrome.driver", ResourceUtil.getResource("chromedriver.exe").getPath());
            System.setProperty("webdriver.http.factory", "jdk-http-client");
            ChromeOptions chromeOptions = new ChromeOptions();
            chromeOptions.addArguments("--remote-allow-origins=*");
            chromeOptions.addArguments("start-maximized");
            webDriver = new ChromeDriver(chromeOptions);
            webDriver.get("https://tpyxhduat.life.cntaiping.com/hdpt/middle-ground/web/mid-bi-track-mgr/index.html#/login");
            WebElement ele = webDriver.findElement(By.xpath("//div[@class='real-form_sms real-form_content']/img"));
            File screenshot = ((TakesScreenshot) webDriver).getScreenshotAs(OutputType.FILE);
            BufferedImage fullImg = ImageIO.read(screenshot);
            //获取位置
            Point point = ele.getLocation();
            // 获取宽高
            int eleWidth = ele.getSize().getWidth();
            int eleHeight = ele.getSize().getHeight();

            BufferedImage eleScreenshot = fullImg.getSubimage(point.getX(), point.getY(),
                    eleWidth, eleHeight);
            ImageIO.write(eleScreenshot, "png", screenshot);


            File screenshotLocation = new File("C:\\Users\\86180\\Desktop\\no1.png");
            FileUtils.copyFile(screenshot, screenshotLocation);
            String s = RuntimeUtil.execForStr("C:\\Users\\86180\\Desktop\\dist\\ocr.exe", "C:\\Users\\86180\\Desktop\\no1.png");
            Pattern pattern = Pattern.compile("识别结果： (\\S+)", Pattern.DOTALL);
            Matcher matcher = pattern.matcher(s);
