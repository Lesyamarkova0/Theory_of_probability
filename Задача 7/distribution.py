import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
import ipywidgets as widgets

plt.style.use('default')

def show_pdf(pdf, xmin, xmax, grid_size, distr_name, **kwargs):
    X = np.linspace(xmin, xmax, grid_size)
    Y = pdf(X, **kwargs)
    ymax = max(Y) + 0.1
    plt.figure(figsize = (6, 3))
    plt.plot(X, Y, lw = 5)
    plt.grid(ls = ':')
    plt.xlabel('Значение', fontsize = 10)
    plt.ylabel('Плотность', fontsize = 10)
    plt.xlim((xmin, xmax))
    plt.ylim((-0.05, ymax))
    title = 'Плотность {}'.format(distr_name)
    plt.title(title.format(**kwargs), fontsize = 14)
    plt.show()
    
def plot_uniform(a = 0, b = 1, n_points = 1000):
    plt.figure(figsize = (6, 3))
    sample = sts.uniform.rvs(loc = a, scale = b - a, size = n_points)
    plt.hist(sample, bins = 30, density = True, 
             alpha = 0.6, label = 'Гистограмма выборки')
    grid = np.linspace(a - (b - a) / 6, b + (b - a) / 6, n_points)
    plt.plot(grid, sts.uniform.pdf(grid, a, b - a), color = 'red',
            lw = 3, label = 'Плотность случайной величины')
    plt.title(r'Случайная величина $X \sim \mathcal{R}$(a, b)', fontsize = 14)
    plt.legend(fontsize = 10, loc = 8)
    plt.grid(ls = ':')
    plt.show()
    print(f'Математическое ожидание: {round(sample.mean(), 3)}, а по формуле: {round((a + b) / 2, 3)}')
    print(f'Дисперсия: {round(sample.var(), 3)}, а по формуле: {round((b - a) ** 2/12, 3)}')
    
def plot_exp(lmbd = 1, n_points = 10000):
    scale = 1 / lmbd
    plt.figure(figsize = (6, 3))
    sample = sts.expon.rvs(scale = scale, size = n_points)
    plt.hist(sample, bins = 30, density = True, alpha = 0.6, label = 'Гистограмма выборки')
    grid = np.linspace(0, 10, n_points)
    plt.plot(grid, sts.expon.pdf(grid, scale = scale), color = 'red',
            lw = 3, label = 'Плотность случайной величины')
    plt.title(r'Exponential ', fontsize = 14)
    plt.legend(fontsize = 10, loc = 0)
    plt.grid(ls = ':')
    plt.show()
    print(f'Математическое ожидаание: {round(sample.mean(), 3):.3f}, а по формуле: {scale:.3f}')
    print(f'Дисперсия: {sample.var():.3f}, а по формуле: {scale**2:.3f}')
    
def plot_norm(a = 0, sigma = 1, n_points = 10000):
    plt.figure(figsize = (6, 3))
    sample = sts.norm.rvs(loc = a, scale = sigma, size = n_points)
    plt.hist(sample, bins = 30, density = True, alpha = 0.6, 
            label = 'Гистограмма выборки')
    grid = np.linspace(a - 3 * sigma, a + 3 * sigma, n_points)
    plt.plot(grid, sts.norm.pdf(grid, a, sigma), color = 'red', lw = 3, 
            label = 'Плотность случайной величины')
    plt.title(r'Нормальная величина $X \sim \mathcal{N}$', fontsize = 10)
    plt.legend(fontsize = 8, loc = 8)
    plt.grid(ls = ':')
    plt.show()
    print(f'Математическое ожидание: {round(sample.mean(), 3)}, а по формуле: {round(a, 3)}')
    print(f'Дисперсия: {round(sample.var(), 3)}, а по формуле: {round(sigma ** 2, 3)}')
    
def plot_chi2(k = 5, n_points = 10000):
    sample = sts.chi2.rvs(df = k, size = n_points)
    plt.figure(figsize = (6, 3))
    plt.hist(sample, bins = 50, density = True, alpha = 0.6, label='Гистограмма выборки')
    x_max = max(20, np.percentile(sample, 99))
    grid = np.linspace(0.01, x_max, n_points)
    plt.plot(grid, sts.chi2.pdf(grid, df=k), color = 'red', lw = 3,
            label = 'Теоретическая плотность')
    plt.title(r'Хи-квадрат распределение с $k = {k}$ степенями свободы'.format(k = k),
             fontsize = 14)
    plt.legend(fontsize = 10, loc = 0)
    plt.grid(ls = ':')
    plt.show()
    print(f'Параметр: k = {k}')
    print(f'Математическое ожидание: {sample.mean():.3f}, а по формуле: {k:.3f}')
    print(f'Дисперсия: {sample.var():.3f}, а по формуле: {2 * k:.3f}')
    
if __name__=='__main__':
    while True:
        print('\nИсследование распределений непрерывных случайных величин')
        print('1. Равномерное распределение')
        print('2. Экспоненциальное распределение')
        print('3. Нормальное распределение')
        print('4. Хи-квадрат распределение')
        print('0. Выход')
        print()
        
        try:
            choice = input('Выберите номер распределения: ')
            if choice == '0':
                print('Выход')
                break
            elif choice == '1':
                print('\nРавномерное распределение')
                show_pdf(pdf = sts.uniform.pdf, xmin=-0.5, xmax=1.5, grid_size = 10000,
                         distr_name=r'$U(0, 1)$', loc=0, scale=1)
                
                ip_rav = widgets.interactive(
                            show_pdf,
                            pdf = widgets.fixed(sts.uniform.pdf),
                            grid_size = widgets.IntSlider(min=25, max=300, step=25,
                                                         value = 100, description = '$grid\_size$'),
                            xmin = widgets.FloatSlider(min = -1, max = 10, step = 0.1, 
                                                      value = 1, description = '$x_{min}=$'),
                            xmax = widgets.FloatSlider(min = 1, max = 20, step = 0.1,
                                                      value = 10, description = '$x_{max}=$'),
                            loc = widgets.FloatSlider(min = 1, max = 15, step = 0.1,
                                                     value = 3, description = '$a=$'),
                            scale = widgets.FloatSlider(min = 0.5, max = 10, step = 0.01,
                                                       value = 1, description = '$b - a=$'),
                            distr_name = r'$U$({loc:.2f}, {loc:.2f} + {scale:.2f})',
                        )

                display(widgets.VBox(ip_rav.children[:2] + ip_rav.children[4:]))
                ip_rav.update()
                
                plot_uniform(20, 60, 10000)

            elif choice == '2':
                print('\nЭкспоненциальное распределение')
                show_pdf(pdf = sts.expon.pdf, xmin = 0, xmax = 10, grid_size = 10000,
                        distr_name = r'$Exp$', scale = 1
                        )
                
                ip_exp = widgets.interactive(
                    show_pdf,
                    pdf = widgets.fixed(sts.expon.pdf),
                    grid_size = widgets.IntSlider(min = 25, max =300, step=25,
                                                 value = 100, description = '$grid\_size$'),
                    xmin = widgets.FloatSlider(min = 0, max = 20, step = 0.1,
                                              value = 0, description = '$x_{min}=$'),
                    xmax = widgets.FloatSlider(min = 1, max = 20, step = 0.1,
                                              value = 10, description = '$x_{max}=$'),
                    scale = widgets.FloatSlider(min = 0, max = 5, step = 0.1,
                                               value = 1, description = '$1/\lambda = $'),
                    distr_name=r'$Exp$({scale:.2f})',
                )

                display(widgets.VBox(ip_exp.children[:2] + ip_exp.children[4:]))
                ip_exp.update()
                
                plot_exp()
                
            elif choice == '3':
                print('\nНормальное распределение')
                show_pdf(pdf = sts.norm.pdf, xmin = 10, xmax = 25, grid_size = 10000,
                    distr_name = r'$N(18, 1)$', loc = 18, scale = 1
                        )

                ip_norm = widgets.interactive(
                    show_pdf,
                    pdf = widgets.fixed(sts.norm.pdf),
                    grid_size = widgets.IntSlider(min =25, max =300, step = 25,
                                                 value = 100, description = '$grid\_size$'),
                    xmin = widgets.FloatSlider(min = -1, max = 10, step = 0.1,
                                              value = 0, description = '$x_{min}=$'),
                    xmax = widgets.FloatSlider(min = 5, max = 25, step = 0.1,
                                              value = 15, description = '$x_{max}=$'),
                    loc = widgets.FloatSlider(min = -1, max = 25, step = 0.1,
                                             value = 10, description = '$a=$'),
                    scale = widgets.FloatSlider(min = 0.01, max = 10, step = 0.01,
                                               value = 1, description = '$\sigma=$'),
                    distr_name = r'$N$({loc:.2f}, {scale:.2f})'
                )

                display(widgets.VBox(ip_norm.children[:2] + ip_norm.children[4:]))
                ip_norm.update()
                
                plot_norm(10, 25)
                
            elif choice == '4':
                print('\nХи-квадрат распределение')
                show_pdf(pdf = sts.chi2.pdf, xmin = 0, xmax = 20, grid_size = 10000,
                        distr_name = r'$Chi^2(k = 5)$', df = 5)
                
                ip_chi2 = widgets.interactive(
                    show_pdf,
                    pdf = widgets.fixed(sts.chi2.pdf),
                    grid_size = widgets.IntSlider(min = 25, max = 300, step = 25,
                                                 value = 100, description = r'$grid\_size$'),
                    xmin = widgets.FloatSlider(min = 0, max = 1, step = 0.1,
                                               value = 0, description = r'$x_{min}=$'),
                    xmax = widgets.FloatSlider(min = 1, max = 30, step = 0.5,
                                              value = 15, description = r'$x_{max}=$'),
                    df = widgets.FloatSlider(min = 1, max = 20, step = 0.5, value = 5,
                                            description = r'$k=$'),
                    distr_name = r'$Chi^2$(k = {df:.1f})'
                )
                
                display(widgets.VBox(ip_chi2.children[:2] + ip_chi2.children[4:]))
                ip_chi2.update()
                
                plot_chi2(k = 10, n_points = 20000)
                
            else:
                print('Неверный выбор. Введите число от 0 до 4')
        except ValueError:
            print('Ошибка')
