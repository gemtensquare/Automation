class Helper {
    
    FilterNews(news, categories) {
        const categoriesSet = new Set(categories);
        let filteredNews = news.filter((item) => categoriesSet.has(item.category));
        return filteredNews;
    }

    getCategoriesNewsCount(data) {
        const count = Object.create(null)
        for (const news of data) {
            count[news.category] = (count[news.category] || 0) + 1
        }
        return count;
    }
}

export default Helper;
