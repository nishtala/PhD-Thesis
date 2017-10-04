\thispagestyle {empty}
\contentsline {chapter}{List of Figures}{xv}{chapter*.5}
\contentsline {chapter}{List of Tables}{xvii}{chapter*.6}
\contentsline {chapter}{Nomenclature}{xxi}{chapter*.8}
\contentsline {part}{I\hspace {1em}Prologue}{1}{part.1}
\contentsline {chapter}{\numberline {1}Introduction}{2}{chapter.1}
\contentsline {section}{\numberline {1.1}Challenges}{3}{section.1.1}
\contentsline {paragraph}{Shared Resource Contention.}{4}{section.1.1}
\contentsline {paragraph}{Data centre particularities.}{4}{section.1.1}
\contentsline {paragraph}{Transition to Heterogeneous processors.}{5}{figure.caption.12}
\contentsline {paragraph}{Scheduling workloads.}{6}{figure.caption.12}
\contentsline {section}{\numberline {1.2}Outline of thesis}{7}{section.1.2}
\contentsline {paragraph}{Estimate and control performance and power.}{7}{section.1.2}
\contentsline {paragraph}{Addressing resource utilisation.}{8}{section.1.2}
\contentsline {chapter}{\numberline {2}Infrastructure}{10}{chapter.2}
\contentsline {section}{\numberline {2.1}Dynamic Power and Performance Management}{11}{section.2.1}
\contentsline {section}{\numberline {2.2}Architectures}{12}{section.2.2}
\contentsline {section}{\numberline {2.3}Performance Monitoring}{14}{section.2.3}
\contentsline {section}{\numberline {2.4}Power Meters}{14}{section.2.4}
\contentsline {section}{\numberline {2.5}Power Efficiency}{15}{section.2.5}
\contentsline {section}{\numberline {2.6}Workloads}{18}{section.2.6}
\contentsline {subsection}{\numberline {2.6.1}Batch Workloads}{18}{subsection.2.6.1}
\contentsline {subsection}{\numberline {2.6.2}Latency-Critical Workloads}{19}{subsection.2.6.2}
\contentsline {paragraph}{Tail latency requirements.}{20}{table.caption.16}
\contentsline {section}{\numberline {2.7}Conclusion}{20}{section.2.7}
\contentsline {part}{II\hspace {1em}Modelling and Prediction Technique}{23}{part.2}
\contentsline {chapter}{\numberline {3}Multicore Power and Performance Modelling}{27}{chapter.3}
\contentsline {section}{\numberline {3.1}Single-Core Offline Modelling}{28}{section.3.1}
\contentsline {subsection}{\numberline {3.1.1}Modelling Power}{31}{subsection.3.1.1}
\contentsline {paragraph}{Predicting power in the current configuration.}{31}{subsection.3.1.1}
\contentsline {paragraph}{Predicting power across DVFS states.}{31}{equation.3.1.1}
\contentsline {paragraph}{Predicting power across Cl-States.}{32}{figure.caption.22}
\contentsline {subsection}{\numberline {3.1.2}Modelling Performance}{33}{subsection.3.1.2}
\contentsline {paragraph}{Reporting performance at current configuration.}{33}{subsection.3.1.2}
\contentsline {paragraph}{Predicting performance across DVFS states.}{34}{subsection.3.1.2}
\contentsline {paragraph}{Predicting performance across Cl-States.}{34}{equation.3.1.3}
\contentsline {subsection}{\numberline {3.1.3}Single-Core Algorithm}{34}{subsection.3.1.3}
\contentsline {subsection}{\numberline {3.1.4}Training the Models}{35}{subsection.3.1.4}
\contentsline {subsection}{\numberline {3.1.5}Trace Files}{36}{subsection.3.1.5}
\contentsline {section}{\numberline {3.2}Multicore Modelling}{37}{section.3.2}
\contentsline {section}{\numberline {3.3}Single-Core Model Evaluation}{40}{section.3.3}
\contentsline {subsection}{\numberline {3.3.1}Model Assessment}{40}{subsection.3.3.1}
\contentsline {subsection}{\numberline {3.3.2}Offline Evaluation}{40}{subsection.3.3.2}
\contentsline {subsection}{\numberline {3.3.3}Online Evaluation}{47}{subsection.3.3.3}
\contentsline {section}{\numberline {3.4}Multicore Model Evaluation}{51}{section.3.4}
\contentsline {subsection}{\numberline {3.4.1}Multicore Models ignoring Contention}{51}{subsection.3.4.1}
\contentsline {subsection}{\numberline {3.4.2}Multicore Models including Contention without Constraints}{52}{subsection.3.4.2}
\contentsline {subsection}{\numberline {3.4.3}Multicore Models including Contention with Constraints}{55}{subsection.3.4.3}
\contentsline {subsubsection}{\numberline {3.4.3.1}REPP Configuration Selector}{55}{subsubsection.3.4.3.1}
\contentsline {subsubsection}{\numberline {3.4.3.2}Experiments}{56}{subsubsection.3.4.3.2}
\contentsline {paragraph}{Enabling Power/Performance Capping.}{60}{table.caption.44}
\contentsline {section}{\numberline {3.5}Conclusion}{61}{section.3.5}
\contentsline {chapter}{\numberline {4}Power and Performance Models with Consolidation}{63}{chapter.4}
\contentsline {section}{\numberline {4.1}Energy Efficient Scheduler}{64}{section.4.1}
\contentsline {subsection}{\numberline {4.1.1}Algorithm Description}{65}{subsection.4.1.1}
\contentsline {section}{\numberline {4.2}Multicore Modelling with Consolidation}{66}{section.4.2}
\contentsline {paragraph}{Core consolidation.}{66}{section.4.2}
\contentsline {paragraph}{Impact on performance and power.}{66}{section.4.2}
\contentsline {paragraph}{Modelling methodology.}{67}{figure.caption.46}
\contentsline {subsection}{\numberline {4.2.1}Is consolidation worth it?}{68}{subsection.4.2.1}
\contentsline {section}{\numberline {4.3}Evaluation}{70}{section.4.3}
\contentsline {subsection}{\numberline {4.3.1}Workloads}{70}{subsection.4.3.1}
\contentsline {subsection}{\numberline {4.3.2}Energy Efficient Scheduler}{70}{subsection.4.3.2}
\contentsline {subsection}{\numberline {4.3.3}Multicore Models including Consolidation with Constraints}{73}{subsection.4.3.3}
\contentsline {section}{\numberline {4.4}Implementation of the Modelling and Prediction Technique}{76}{section.4.4}
\contentsline {paragraph}{Algorithm Configuration.}{76}{section.4.4}
\contentsline {paragraph}{Scalability.}{76}{section.4.4}
\contentsline {section}{\numberline {4.5}Conclusion}{79}{section.4.5}
\contentsline {part}{III\hspace {1em}Addressing scheduling of interactive and batch workloads}{81}{part.3}
\contentsline {chapter}{\numberline {5}Hybrid Task Manager for Interactive Workloads}{82}{chapter.5}
\contentsline {section}{\numberline {5.1}Motivation}{84}{section.5.1}
\contentsline {paragraph}{Mixing different core types with DVFS.}{84}{figure.caption.55}
\contentsline {paragraph}{Exploring workload particularities.}{86}{figure.caption.56}
\contentsline {section}{\numberline {5.2}Hipster}{88}{section.5.2}
\contentsline {subsection}{\numberline {5.2.1}Hipster Reinforcement Learning}{88}{subsection.5.2.1}
\contentsline {subsection}{\numberline {5.2.2}Hipster Design}{90}{subsection.5.2.2}
\contentsline {subsection}{\numberline {5.2.3}Heuristic Mapper (Learning Phase)}{91}{subsection.5.2.3}
\contentsline {subsection}{\numberline {5.2.4}Reward Calculation}{92}{subsection.5.2.4}
\contentsline {subsection}{\numberline {5.2.5}Exploitation Phase}{94}{subsection.5.2.5}
\contentsline {subsection}{\numberline {5.2.6}Responsiveness and Stability}{96}{subsection.5.2.6}
\contentsline {subsection}{\numberline {5.2.7}Hipster Implementation}{96}{subsection.5.2.7}
\contentsline {paragraph}{QoS Monitor.}{96}{subsection.5.2.7}
\contentsline {paragraph}{Mapper Module.}{96}{subsection.5.2.7}
\contentsline {paragraph}{Runtime overhead.}{97}{subsection.5.2.7}
\contentsline {paragraph}{Lookup table.}{97}{figure.caption.59}
\contentsline {section}{\numberline {5.3}Evaluation}{98}{section.5.3}
\contentsline {subsection}{\numberline {5.3.1}Algorithm Configuration}{98}{subsection.5.3.1}
\contentsline {subsection}{\numberline {5.3.2}HipsterIn Results}{98}{subsection.5.3.2}
\contentsline {subsubsection}{\numberline {5.3.2.1}Hipster's Heuristic Policy (interactive only)}{98}{subsubsection.5.3.2.1}
\contentsline {subsubsection}{\numberline {5.3.2.2}HipsterIn: Memcached Results}{100}{subsubsection.5.3.2.2}
\contentsline {subsubsection}{\numberline {5.3.2.3}HipsterIn: Web-Search Results}{100}{subsubsection.5.3.2.3}
\contentsline {subsubsection}{\numberline {5.3.2.4}\textbf {HipsterIn: Swapping applications}}{101}{subsubsection.5.3.2.4}
\contentsline {subsubsection}{\numberline {5.3.2.5}HipsterIn Summary}{101}{subsubsection.5.3.2.5}
\contentsline {subsubsection}{\numberline {5.3.2.6}HipsterIn Analysis}{102}{subsubsection.5.3.2.6}
\contentsline {subsection}{\numberline {5.3.3}HipsterCo Results}{106}{subsection.5.3.3}
\contentsline {section}{\numberline {5.4}Deployment Methodology for New Workloads}{108}{section.5.4}
\contentsline {subsection}{\numberline {5.4.1}System profiling}{108}{subsection.5.4.1}
\contentsline {subsection}{\numberline {5.4.2}Hipster runtime}{109}{subsection.5.4.2}
\contentsline {section}{\numberline {5.5}Conclusion}{109}{section.5.5}
\contentsline {part}{IV\hspace {1em}Epilogue}{111}{part.4}
\contentsline {chapter}{\numberline {6}Related Work}{112}{chapter.6}
\contentsline {section}{\numberline {6.1}Performance and Power Modelling}{113}{section.6.1}
\contentsline {section}{\numberline {6.2}Energy Efficient Scheduling}{115}{section.6.2}
\contentsline {section}{\numberline {6.3}QoS Guarantees for Interactive Workloads}{116}{section.6.3}
\contentsline {chapter}{\numberline {7}Conclusion}{119}{chapter.7}
\contentsline {chapter}{\numberline {8}Future Directions}{122}{chapter.8}
\contentsline {paragraph}{Multithreaded workloads for REPP.}{122}{chapter.8}
\contentsline {paragraph}{Scaling Hipster on larger infrastructures.}{123}{chapter.8}
\contentsline {paragraph}{Request-level QoS guarantee.}{123}{chapter.8}
\contentsline {paragraph}{Distributed workloads for REPP and Hipster.}{123}{chapter.8}
\contentsline {chapter}{Appendix \numberline {A}Multiprogrammed benchmarks}{125}{Appendix.a.A}
\contentsline {part}{V\hspace {1em}Bibliography}{127}{part.5}
\contentsline {chapter}{References}{128}{chapter*.73}
